import json, sys, time, urllib.request, urllib.parse, collections
UA = "m2-spec-research/0.1 (https://github.com/tamnd/math2-agent)"
proj, out = sys.argv[1], sys.argv[2]
rows, cont = [], {}
while True:
    q = {"action":"query","list":"projectpages","wppprojects":proj,"wpplimit":"500","wppassessments":"1","format":"json"}
    q.update(cont)
    req = urllib.request.Request("https://en.wikipedia.org/w/api.php?"+urllib.parse.urlencode(q), headers={"User-Agent":UA})
    d = json.load(urllib.request.urlopen(req))
    rows += d["query"]["projects"].get(proj, [])
    if "continue" not in d: break
    cont = d["continue"]; time.sleep(0.5)
json.dump(rows, open(out,"w"))
ns = collections.Counter(r["ns"] for r in rows)
cl = collections.Counter(r.get("assessment",{}).get("class","") for r in rows if r["ns"]==0)
im = collections.Counter(r.get("assessment",{}).get("importance","") for r in rows if r["ns"]==0)
print(proj, len(rows), "ns:", dict(ns)); print(" class(ns0):", dict(cl)); print(" importance(ns0):", dict(im))
