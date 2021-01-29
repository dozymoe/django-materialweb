# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= ../run pybin sphinx-build
SPHINXAPIDOC  ?= ../run sphinx-apidoc
SOURCEDIR     = ../docs
BUILDDIR      = ../docs_build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

api:
	@SPHINX_APIDOC_OPTIONS=members $(SPHINXAPIDOC)\
			--output-dir=docs/gen -eEfMT materialweb\
		    materialweb/templatetags/ materialweb/tests/\
			materialweb/tests.py materialweb/apps.py\
			materialweb/tags/base.py

.PHONY: help Makefile api

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile api
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
