# Sphinx Spelling Checker Extension

[sphinxcontrib spelling checker](https://sphinxcontrib-spelling.readthedocs.io/en/latest/)

> :warning: Only available for Linux\
> `pyenchant is broken on Windows`

## Run spelling checker

Assuming you are already inside python virtual environment.

To run the spelling checker on your local `vicharak-docs` source, use following command:

```bash
make spelling -j$(nproc --all)
```

<details><summary>Click to see output</summary>

```
(vicharak-docs) ┌─[vicharak@galactos-bubuntu] in ~/vicharak-docs on utsav
└─[󰄛] make spelling -j32                             
sphinx-build -b spelling "source" "_build"  
Running Sphinx v6.2.1
Initializing Spelling Checker 8.0.0
loading pickled environment... done
Ignoring wiki words
Ignoring acronyms
Adding package names from PyPI to local dictionary…
Ignoring Python builtins
Ignoring importable module names
Ignoring contributor names
Looking for custom word list in /home/vicharak/vicharak-docs/source/spelling_wordlist.txt
Scanning contributors
myst v2.0.0: MdParserConfig(commonmark_only=False, gfm_only=False, enable_extensions={'strikethrough', 'tasklist', 'deflist', 'colon_fence', 'smartquotes', 'linkify', 'attrs_block', 'attrs_inline'}, disable_syntax=[], all_links_external=False, url_schemes=('http', 'https', 'mailto', 'ftp'), ref_domains=None, fence_as_directive=set(), number_code_blocks=[], title_to_header=True, heading_anchors=4, heading_slug_func=None, html_meta={}, footnote_transition=True, words_per_minute=200, substitutions={}, linkify_fuzzy_links=True, dmath_allow_labels=True, dmath_allow_space=True, dmath_allow_digits=True, dmath_double_inline=False, update_mathjax=True, mathjax_classes='tex2jax_process|mathjax_process|math|output_area', enable_checkboxes=False, suppress_warnings=[], highlight_code_blocks=True)
building [mo]: targets for 0 po files that are out of date
writing output... 
building [spelling]: all documents
updating environment: 0 added, 1 changed, 0 removed
reading sources... [100%] downloads                                                                                                                                        
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
source/downloads.rst:7: : Spell check: Datasheets: ["Data sheets", "Data-sheets", "Dustsheets"]: Datasheets.                                                               
source/downloads.rst:20: : Spell check: Pinouts: ["Pin outs", "Pin-outs", "Outpoints"]: Vaaman Pinouts Guide.
Writing /home/vicharak/vicharak-docs/_build/downloads.spelling
writing output... [100%] vaaman-sdk                                                                                                                                        
WARNING: Found 2 misspelled words
build succeeded, 1 warning.
```

</details>

In the above output there were two spelling mistakes found.

```
source/downloads.rst:7: : Spell check: Datasheets: ["Data sheets", "Data-sheets", "Dustsheets"]: Datasheets.                                                               
source/downloads.rst:20: : Spell check: Pinouts: ["Pin outs", "Pin-outs", "Outpoints"]: Vaaman Pinouts Guide.
```

For the above two spelling mistakes, You can accept the suggestions provided by the spelling checker.

Replace `Datasheets` with `Data-sheets`.

Replace `Pinouts` with `Pin-outs`.
