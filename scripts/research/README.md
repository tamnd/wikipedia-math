# Research scripts

These scripts made the measurements in the Wikipedia spec (WP01 to WP04). They use the Action API of English Wikipedia and the Wikidata API, with a User-Agent that names the project. They are kept so that each number in the spec can be made again. The production code is in `tamnd/wikipedia-cli` and `tamnd/math2-agent`, not here.

Each script reads a JSON or text file and writes one JSON file. They need Python 3 and no other packages.

| Script | Input | Output |
|---|---|---|
| `projpages.py PROJECT OUT` | the name of a WikiProject, such as `Mathematics` | the pages of the project, with their assessment class and importance |
| `resolve.py TITLES OUT` | a file with one title on each line | for each title: the target after redirects, the Wikidata id, and the disambiguation flag |
| `props.py TITLES OUT` | a file with one title on each line | for each title: the categories that are not hidden, and the Wikidata id |
| `p31.py PAGES OUT` | the output of `projpages.py` | the Wikidata id of each article, and its P31 classes |
| `wikitext.py PAGES OUT N` | the output of `projpages.py` | the wikitext of a random sample of N articles. The seed is 2148, so the sample is the same each time |

The sample of 400 articles in the spec is `wikitext.py math.json sample_wt.json 400`, where `math.json` is `projpages.py Mathematics math.json`. The Wikidata API limits the rate of requests. When it answers 429, wait and run the script again.
