# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SOURCEDIR     = source
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	sphinx-build -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help spelling mdspell clean Makefile

spelling:
	sphinx-build -b spelling "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

mdspell:
	ifeq (, $(shell which mdspell))
		$(error "No mdspell package installed, consider installing it with 'npm install -g markdown-spellcheck'")
	endif
	find source -type f -name \*.md -exec mdspell - {} \;

clean:
	rm -rf ${BUILDDIR}

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	sphinx-build -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
