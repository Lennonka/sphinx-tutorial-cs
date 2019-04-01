# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Projekt'
copyright = '2018, Autor'
author = 'Autor'

# The short X.Y version
version = '1.0'
# The full version, including alpha/beta/rc tags
release = version

#today_fmt = '%d.%m.%Y'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
#needs_sphinx = '2.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'cs'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.git']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# Globální substituce
rst_prolog = """
.. |author| replace:: {author}
""".format(author=author)

rst_epilog = """
.. |lpage| raw:: latex

    \\newpage
.. |br| raw:: html

    <br />

.. |lbr| raw:: latex

    \\newline
"""

# IFconfig - only
#tags.add('extra')

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bizstyle'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'mytheme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# Moje přizpůsobení
#html_css_files = ['moje.css']
#html_secnumber_suffix = ' '
#html_title = project + ' v' + version
#html_last_updated_fmt = today_fmt
#html_show_copyright = False # např. pro copyleft nebo public domain projekty

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',

    ###
    #'papersize': 'a4paper',
    #'fontpkg': '\\usepackage[sfdefault]{roboto}',
    #'fncychap': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Projekt.tex', 'Projekt Documentation', 'Autor', 'manual'), # default grouping
    # grouping by book
    #('Kniha/index', 'Projekt-Kniha.tex', 'Kniha o Projektu', author, 'manual', False)
]

# Topmost sectioning unit: 'part', 'chapter' or 'section' (default)
#latex_toplevel_sectioning = 'chapter'
# Printed - add page references after internal references
#latex_show_pagerefs = True
# Printed - display URLs: 'no' (default), 'footnote', 'inline'
#latex_show_urls = 'footnote'
