import json, sys, time, urllib.request, urllib.parse
UA = "m2-spec-research/0.1 (https://github.com/tamnd/math2-agent)"
def get(url,q):
    for a in range(5):
        try:
            req=urllib.request.Request(url,data=urllib.parse.urlencode(q).encode(),headers={"User-Agent":UA})
            return json.load(urllib.request.urlopen(req,timeout=60))
        except Exception as e: time.sleep(5*(a+1))
    raise SystemExit("fail")
rows=json.load(open(sys.argv[1]))
titles=[r["title"] for r in rows if r["ns"]==0 and r.get("assessment",{}).get("class") not in ("Redirect","Disambig")]
qid={}
for i in range(0,len(titles),50):
    d=get("https://en.wikipedia.org/w/api.php",{"action":"query","titles":"|".join(titles[i:i+50]),"prop":"pageprops","ppprop":"wikibase_item","format":"json","formatversion":"2"})
    for p in d["query"]["pages"]: qid[p["title"]]=p.get("pageprops",{}).get("wikibase_item")
    time.sleep(0.35)
ids=[q for q in qid.values() if q]; p31={}
for i in range(0,len(ids),50):
    d=get("https://www.wikidata.org/w/api.php",{"action":"wbgetentities","ids":"|".join(ids[i:i+50]),"props":"claims","format":"json"})
    for k,e in d.get("entities",{}).items():
        p31[k]=[c["mainsnak"].get("datavalue",{}).get("value",{}).get("id") for c in e.get("claims",{}).get("P31",[])]
    time.sleep(0.35)
json.dump({"qid":qid,"p31":p31},open(sys.argv[2],"w")); print(len(qid),len(p31))
