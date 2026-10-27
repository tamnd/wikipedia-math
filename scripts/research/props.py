# for a title list: non-hidden categories, wikibase item; 50/request
import json, sys, time, urllib.request, urllib.parse
UA = "m2-spec-research/0.1 (https://github.com/tamnd/math2-agent)"
titles=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out={}
for i in range(0,len(titles),50):
    chunk=titles[i:i+50]; cont={}
    while True:
        q={"action":"query","titles":"|".join(chunk),"prop":"categories|pageprops","clshow":"!hidden","cllimit":"max","ppprop":"wikibase_item","format":"json","formatversion":"2"}; q.update(cont)
        req=urllib.request.Request("https://en.wikipedia.org/w/api.php",data=urllib.parse.urlencode(q).encode(),headers={"User-Agent":UA})
        d=json.load(urllib.request.urlopen(req))
        for p in d["query"]["pages"]:
            o=out.setdefault(p["title"],{"cats":[],"qid":None})
            o["cats"]+= [c["title"][9:] for c in p.get("categories",[])]
            o["qid"]=o["qid"] or p.get("pageprops",{}).get("wikibase_item")
        if "continue" not in d: break
        cont=d["continue"]; time.sleep(0.3)
    time.sleep(0.3)
json.dump(out,open(sys.argv[2],"w"))
