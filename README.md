# wikipedia-math

This repository is the Wikipedia corpus of math2. It holds the mathematics articles of English Wikipedia in the form that math2 needs: the metadata of each article, its wikitext at one revision, and the objects that the extractor finds in it. The goal is that each mathematical item of each article in scope (each definition, statement, proof and example) reaches an outcome in math2, and that a person can check this.

The design is in the Wikipedia spec of math2 (WP01 to WP15). The tools that fill this repository are `wiki` from [tamnd/wikipedia-cli](https://github.com/tamnd/wikipedia-cli) and `m2` from [tamnd/math2-agent](https://github.com/tamnd/math2-agent).

## Layout

| Path | Holds |
|---|---|
| `manifests/wikipedia/templates.yaml` | the template table (WP3.2): the class of each template and the roles of its parameters |
| `manifests/wikipedia/headings.yaml` | the heading table (WP3.5): the section role of each heading |
| `manifests/wikipedia/texvc.yaml` | the texvc macros and their standard TeX (WP3.3) |
| `manifests/wikipedia/classes.yaml` | the Wikidata classes and identifiers of signal S5 (WP1.2) |
| `manifests/wikipedia/waivers.yaml` | the waivers of the census (WP4.8) |
| `manifests/wikipedia/categories.yaml` | the category roots, the exclusions and the keywords of signal S6 (WP1.2) |
| `manifests/wikipedia/candidates.tsv` | each candidate page with its signals, its verdict and its rule (WP1.3) |
| `manifests/wikipedia/scope.tsv` | the state of each page in scope (WP1.4) |
| `manifests/wikipedia/verdicts.tsv` | the verdicts of the scope model pass for the candidates that the rules do not decide (WP7.2) |
| `manifests/wikipedia/stopped.tsv` | the pages that left the scope, with the reason (WP1.4) |
| `manifests/wikipedia/gold/scope.tsv` | gold set S, the marked sample that measures the scope list (WP11.2) |
| `reports/scope.md` and `reports/gold-s.md` | the reports of `m2 wp scope` and `m2 wp gold measure` |
| `scripts/scope/llm.py` | the script of the scope model pass and of the draft marks of gold set S |
| `manifests/wikipedia/pilot.txt` | the titles of the 20 articles of the group theory pilot (WP-M0) |
| `metadata/<shard>.jsonl` | one record for each article in scope |
| `content/wikitext/<shard>/<pageid>.wiki` | the wikitext of the revision of record, with a header |
| `content/markdown/<shard>/<pageid>.md` | the Markdown rendering, with the licence header |
| `analysis/objects/<shard>/<pageid>-r<revision>.jsonl` | the object records (WP3.13) |
| `analysis/census/<shard>/<pageid>-r<revision>.json` | the census records (WP4.5) |
| `scripts/research/` | the scripts that made the measurements of the spec |
| `work/` | the downloads and the table store. This directory is not committed |

`<shard>` is the page id divided by 10,000, with zeros in front to 4 digits. For example, page 53993 is in shard `0005`. Page ids do not change, so an article stays in its shard.

## Content header

Each file in `content/` starts with a header that gives the source and the licence of its text:

```
<!-- wikipedia: en
     page: <pageid>
     title: <title>
     revision: <revision>
     timestamp: <timestamp>
     history: https://en.wikipedia.org/w/index.php?curid=<pageid>&action=history
     licence: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
     source: https://en.wikipedia.org/w/index.php?oldid=<revision> -->
```

The history link lists the authors of the article.

## Extraction

`m2 wp extract` fetches an article, writes its content file, and writes its objects file and its census file. The census file names the version of `m2` that made it. Use a release build of `m2`, not a development build, for the files that you commit.

```
$ m2 wp extract -corpus . -list manifests/wikipedia/pilot.txt
$ m2 wp extract -corpus .            # extract the content plane again
```

Run the audit from a checkout of tamnd/math2, because it writes its report there:

```
$ m2 audit -wikipedia ../wikipedia-math -group Y -hard
```

The group theory pilot has 20 articles. With m2 v0.3.8 it gives 1183 objects and 263 counted cues, and each cue has an object. The Y rules of the audit give no finding.

## Licence

The text of the articles is under CC BY-SA 4.0, as on Wikipedia. The metadata, the analysis records, the manifests and the scripts are under CC0 1.0. See `LICENSE.md` for which path has which licence.
