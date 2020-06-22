# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import datetime

# import sphinx_rtd_theme
# import picard_theme

this_year = datetime.datetime.now().year
copyright_year = str(this_year) if this_year == 2020 else '2020-{0}'.format(this_year)

# -- Project information -----------------------------------------------------

project = 'MusicBrainz Picard'
# copyright = 'MusicBrainz Picard User Guide by Bob Swift is licensed under CC0 1.0. To view a copy of this license, visit https://creativecommons.org/publicdomain/zero/1.0'
copyright = 'This documentation is licensed under CC0 1.0.'
author = 'Bob Swift'

# The full version, including alpha/beta/rc tags
release = 'v2.3.2'
version = release

# -- Notice for Back of Title Page in LaTex Output ---------------------------

my_notice = r'''\vspace*{\fill}
MusicBrainz Picard User Guide by Bob Swift is licensed under CC0 1.0. To view a
copy of this license, visit https://creativecommons.org/publicdomain/zero/1.0
\vspace{0.1\textheight}'''


# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    # "sphinx_rtd_theme",
    # "picard_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'README.md',
    'html',
    'docs',
    'locale',
    '.git',
    '.github',
    'images',
    'testing',
    'README.md',
    'TODO.md',
]


# -- Options for Internationalization ----------------------------------------

language = 'en'
locale_dirs = ['locale']
gettext_compact = False
# gettext_compact = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
# html_theme = "picard_theme"
# html_theme = "basic"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'extra_css_files': [
        '_static/css/extra.css',
    ],
    'supported_languages': [
        ('en', 'English'),
        # ('fr', 'Française'),
        # ('de', 'Deutsche'),
        # ('es', 'Española'),
    ]
}

html_favicon = '_static/picard-icon.png'


# -- Options for LaTeX / PDF output ------------------------------------------

latex_documents = [
    ('pdf', 'musicbrainzpicard.tex', 'MusicBrainz Picard', '', 'manual', False),
    # ('pdf', 'musicbrainzpicard.tex', 'MusicBrainz Picard', 'Edited by Bob Swift', 'manual', False),
    # ('pdf', 'musicbrainzpicard.tex', 'MusicBrainz Picard', '', 'howto', False),
]

# latex_toplevel_sectioning = 'part'
# latex_toplevel_sectioning = 'section'     # Use with 'howto' document style
# latex_toplevel_sectioning = 'chapter'

# latex_show_urls = 'inline'
latex_show_urls = 'footnote'
# latex_show_urls = 'no'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    # 'preamble': '\\hyphenation{Music-Brainz}',
    'preamble': r'''\hyphenation{Music-Brainz}
    \newcommand\sphinxbackoftitlepage{''' + my_notice + r'''}
    ''',
    'extraclassoptions': 'openany',
    # 'maketitle': r'\newcommand\sphinxbackoftitlepage{<Extra material>}\sphinxmaketitle',
    # 'maketitle': r'\newcommand\sphinxbackoftitlepage{<Extra material>}\sphinxmaketitle',
}

latex_domain_indices = True


# -- Options for epub output ------------------------------------------

# epub_baseneme = 'musicbrainzpicard'

epub_theme = 'epub'

epub_description = 'A User Guide for MusicBrainz Picard.'

epub_author = 'Bob Swift'

epub_contributor = 'Members of the MusicBrainz Community'

epub_uid = 'MusicBrainzPicardUserGuide'

epub_cover = ('_static/epub_cover.png', 'epub-cover.html')
# epub_cover = ('_static/epub_cover.png', '')

# epub_show_urls = 'inline'
epub_show_urls = 'footnote'
# epub_show_urls = 'no'

epub_use_index = True
