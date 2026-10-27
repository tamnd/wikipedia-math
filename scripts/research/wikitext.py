import json, sys, time, random, urllib.request, urllib.parse
UA = "m2-spec-research/0.1 (https://github.com/tamnd/math2-agent)"
rows=json.load(open(sys.argv[1])); random.seed(2148)
arts=[r["title"] for r in rows if r["ns"]==0 and r.get("assessment",{}).get("class") not in ("Redirect","Disambig")]
sample=random.sample(arts,int(sys.argv[3])); out={}
for i in range(0,len(sample),50):
    q={"action":"query","titles":"|".join(sample[i:i+50]),"prop":"revisions","rvprop":"content|ids","rvslots":"main","format":"json","formatversion":"2"}
    req=urllib.request.Request("https://en.wikipedia.org/w/api.php",data=urllib.parse.urlencode(q).encode(),headers={"User-Agent":UA})
    d=json.load(urllib.request.urlopen(req))
    for p in d["query"]["pages"]:
        if "revisions" in p: out[p["title"]]=p["revisions"][0]["slots"]["main"]["content"]
    time.sleep(1)
json.dump(out,open(sys.argv[2],"w")); print(len(out))
