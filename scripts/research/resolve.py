# resolve titles (redirects, normalization) via the action API, 50 per request; also get pageprops wikibase_item and disambiguation
import json, sys, time, urllib.request, urllib.parse
UA = "m2-spec-research/0.1 (https://github.com/tamnd/math2-agent)"
titles=[l.strip() for l in open(sys.argv[1]) if l.strip()]
res={}
for i in range(0,len(titles),50):
    chunk=titles[i:i+50]
    q={"action":"query","titles":"|".join(chunk),"redirects":"1","prop":"pageprops","ppprop":"wikibase_item|disambiguation","format":"json","formatversion":"2"}
    req=urllib.request.Request("https://en.wikipedia.org/w/api.php",data=urllib.parse.urlencode(q).encode(),headers={"User-Agent":UA})
    d=json.load(urllib.request.urlopen(req))["query"]
    m={t:t for t in chunk}
    for n in d.get("normalized",[]): m={k:(n["to"] if v==n["from"] else v) for k,v in m.items()}
    for r in d.get("redirects",[]): m={k:(r["to"] if v==r["from"] else v) for k,v in m.items()}
    pages={p["title"]:p for p in d["pages"]}
    for k,v in m.items():
        p=pages.get(v,{})
        res[k]={"to":v,"missing":"missing" in p or "invalid" in p,"qid":p.get("pageprops",{}).get("wikibase_item"),"disambig":"disambiguation" in p.get("pageprops",{})}
    time.sleep(0.4)
json.dump(res,open(sys.argv[2],"w"))
