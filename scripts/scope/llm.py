"""The scope model pass (WP7.2) and the draft marks of gold set S, with chatgpt-tool.

Usage:
  python3 llm.py verdicts manifests/wikipedia/candidates.tsv OUT.tsv WORKDIR [SHARD/SHARDS]
  python3 llm.py gold manifests/wikipedia/gold/scope.tsv WORKDIR

verdicts asks the model about each candidate with the verdict pending, and
writes the rows of verdicts.tsv to OUT.tsv. With SHARD/SHARDS (for example
1/2), it takes only one part of the candidates, so that two hosts can run at
the same time. Join the parts and copy them to manifests/wikipedia/verdicts.tsv,
then run m2 wp scope again.

gold writes a draft mark into each row of gold set S that has no mark. The
marker of these rows is chatgpt-draft. A person must check each draft mark
and write their name as the marker. The marks of gold set S must not come
only from the model, because the model pass is one of the things that gold
set S measures.

When chatgpt-tool fails, the script stops. Log the session in again (for
example with chatgpt-tool heal-sessions) and run the script again.

The script keeps the extracts and the answers in WORKDIR, so a second run
continues where the first run stopped.
"""

import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

UA = "math2-agent-scope/0.1 (https://github.com/tamnd/math2-agent)"
API = "https://en.wikipedia.org/w/api.php"
TOOL = os.environ.get("CHATGPT_TOOL", "chatgpt-tool")
BATCH = 80
# PAUSE is the wait in seconds after each question. A session that asks
# without a pause is signed out sooner.
PAUSE = int(os.environ.get("PAUSE", "0"))
MARKS = ("math", "uses-math", "not-math")
CONFIDENCE = {"high": 0.9, "low": 0.65}

PROMPT = """You decide which Wikipedia articles go into a corpus of mathematics. For each article below, give one verdict:

math: the article states, defines or proves mathematics, or it is about a mathematical object, method, field, problem, history, or a person who is known for mathematics.
uses-math: the article is about another subject, such as physics, engineering, economics, chemistry or computing, and it uses mathematics as a tool. The subject itself is not mathematics.
not-math: the article is not about mathematics. Countries, cities, universities, companies, general science, writing systems and Unicode blocks are not-math, unless the article is about their mathematics.

Each article has its page id, its title and its first sentences. Reply with one line for each article and nothing else. Each line has four parts with a tab between them: the page id, the verdict, high or low for how sure you are, and a reason of at most ten words.

"""


def get(params):
    params = dict(params, format="json", formatversion="2")
    for attempt in range(5):
        try:
            req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception:
            time.sleep(5 * (attempt + 1))
    raise SystemExit("the Action API does not answer")


def extracts(ids, cache):
    out = json.load(open(cache)) if os.path.exists(cache) else {}
    todo = [i for i in ids if i not in out]
    for k in range(0, len(todo), 20):
        d = get({"action": "query", "prop": "extracts", "exintro": 1, "explaintext": 1, "exsentences": 2, "exlimit": 20, "pageids": "|".join(todo[k:k + 20])})
        for p in d["query"]["pages"]:
            out[str(p["pageid"])] = " ".join(p.get("extract", "").split())[:400]
        if k % 1000 == 0:
            json.dump(out, open(cache, "w"))
            print("extracts: %d of %d" % (k, len(todo)), flush=True)
        time.sleep(0.2)
    json.dump(out, open(cache, "w"))
    return out


def ask(batch, text, work, n):
    """batch is a list of (page id, title). It gives page id -> (verdict, sure, reason)."""
    answer = os.path.join(work, "answer-%04d.txt" % n)
    if not os.path.exists(answer) or os.path.getsize(answer) == 0:
        prompt = os.path.join(work, "prompt-%04d.md" % n)
        with open(prompt, "w") as f:
            f.write(PROMPT)
            for pid, title in batch:
                f.write("%s\t%s\t%s\n" % (pid, title.replace("_", " "), text.get(pid, "")))
        r = subprocess.run([TOOL, "ask", "--prompt-file", prompt, "--out", answer, "--no-verbose"])
        if r.returncode != 0:
            # The session is often signed out. Stop, so that the caller can
            # log it in again, and run the script again to continue.
            sys.exit("batch %d: chatgpt-tool failed" % n)
        time.sleep(PAUSE)
    out = {}
    for line in open(answer):
        f = [x.strip().strip("`") for x in line.strip().split("\t")]
        if len(f) >= 2 and f[1] in MARKS:
            sure = f[2].lower() if len(f) > 2 and f[2].lower() in CONFIDENCE else "low"
            out[f[0]] = (f[1], sure, f[3] if len(f) > 3 else "")
    return out


def verdicts(src, dst, work, shard):
    rows = [l.rstrip("\n").split("\t") for l in open(src)][1:]
    todo = [(r[0], r[1]) for r in rows if r[8] == "pending"]
    k, n = (int(x) for x in shard.split("/"))
    todo = [t for i, t in enumerate(todo) if i % n == k - 1]
    os.makedirs(work, exist_ok=True)
    text = extracts([t[0] for t in todo], os.path.join(work, "extracts.json"))
    have = {}
    if os.path.exists(dst):
        for l in list(open(dst))[1:]:
            have[l.split("\t")[0]] = l
    for b, i in enumerate(range(0, len(todo), BATCH)):
        batch = [t for t in todo[i:i + BATCH] if t[0] not in have]
        if not batch:
            continue
        got = ask(batch, text, work, b)
        for pid, title in batch:
            if pid in got:
                v, sure, reason = got[pid]
                have[pid] = "%s\t%s\t%s\t%.2f\tchatgpt\t%s\n" % (pid, title, v, CONFIDENCE[sure], reason.replace("\t", " "))
        with open(dst + ".tmp", "w") as f:
            f.write("page_id\ttitle\tverdict\tconfidence\tmodel\tnote\n" + "".join(have[p] for p in sorted(have, key=int)))
        os.replace(dst + ".tmp", dst)
        print("batch %d: %d of %d candidates have a verdict" % (b + 1, len(have), len(todo)), flush=True)


def gold(path, work):
    lines = open(path).read().rstrip("\n").split("\n")
    header, rows = lines[0], [l.split("\t") for l in lines[1:]]
    todo = [r for r in rows if r[6] == ""]
    os.makedirs(work, exist_ok=True)
    text = extracts([r[0] for r in todo], os.path.join(work, "extracts.json"))
    for b, i in enumerate(range(0, len(todo), BATCH)):
        batch = todo[i:i + BATCH]
        got = ask([(r[0], r[1]) for r in batch], text, work, b)
        for r in batch:
            if r[0] in got:
                r[6], r[7], r[8] = got[r[0]][0], "chatgpt-draft", got[r[0]][2].replace("\t", " ")
        with open(path + ".tmp", "w") as f:
            f.write(header + "\n" + "".join("\t".join(r) + "\n" for r in rows))
        os.replace(path + ".tmp", path)
        print("batch %d done" % (b + 1), flush=True)


if __name__ == "__main__":
    if len(sys.argv) >= 5 and sys.argv[1] == "verdicts":
        verdicts(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "1/1")
    elif len(sys.argv) == 4 and sys.argv[1] == "gold":
        gold(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
