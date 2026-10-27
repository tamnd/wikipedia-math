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
| `metadata/<shard>.jsonl` | one record for each article in scope |
| `content/wikitext/<shard>/<pageid>.wiki` | the wikitext of the revision of record, with a header |
| `content/markdown/<shard>/<pageid>.md` | the Markdown rendering, with the licence header |
| `analysis/objects/<shard>/<pageid>.jsonl` | the object records (WP3.13) |
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

## Licence

The text of the articles is under CC BY-SA 4.0, as on Wikipedia. The metadata, the analysis records, the manifests and the scripts are under CC0 1.0. See `LICENSE.md` for which path has which licence.
