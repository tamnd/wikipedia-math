# Licence

This repository has two licences. The licence of a file depends on its path.

## Text: CC BY-SA 4.0

These paths hold text from English Wikipedia:

- `content/wikitext/`
- `content/markdown/`

This text is under the Creative Commons Attribution-ShareAlike 4.0 International licence (CC BY-SA 4.0), https://creativecommons.org/licenses/by-sa/4.0/. The authors are the editors of each article. The header of each file gives the title, the revision, a link to that revision, and a link to the history page of the article, which lists the authors. If you use this text, keep this attribution and use the same licence for what you make from it.

The `text` fields of the object records in `analysis/objects/` are spans of the same text. They have the same licence and the same attribution, through the page id and the revision in each record.

## Everything else: CC0 1.0

All other files are under CC0 1.0 Universal, https://creativecommons.org/publicdomain/zero/1.0/. This includes the metadata in `metadata/`, the structure and the counts in `analysis/` (except the `text` fields above), the manifests in `manifests/`, the reports in `reports/` and the scripts in `scripts/`. To the extent possible under law, the authors give up all copyright and related rights in these files.

Facts about an article (its title, its page id, its categories, its links and the positions of its objects) are not text of the article, so they are in this part.
