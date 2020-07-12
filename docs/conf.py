# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
#import inspect
#cwd = os.getcwd()
#project_root = os.path.dirname(cwd)
#sys.path.insert(0, project_root)

from .. import autodqm
from .. import autoref

# -- Project information -----------------------------------------------------

project = 'AutoDQM'
copyright = '2020, CMS Collaboration'
author = 'CMS Collaboration'

# The full version, including alpha/beta/rc tags
release = '127.0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib-blockdiag',
   'sphinxcontrib-apidoc',
   'sphinxcontrib-programoutput',
   'sphinx-rtd-theme',
   'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Suffixes of source filenames
from recommonmark.parser import CommonMarkParser
source_parsers = {".md": CommonMarkParser}
source_suffix = ['.rst','.md']

# Master toctree document
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

htmlhelp_basename = 'auto-dqm-doc'

# Configure the sphinxcontrib.apidoc extension
apidoc_module_dir = '../autodqm'
apidoc_toc_file = False
apidoc_module_first = True
apidoc_separate_modules = True
pidoc_extra_args = ["-e"]
