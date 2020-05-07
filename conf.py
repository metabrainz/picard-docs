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
import datetime
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# import sphinx_rtd_theme
# import picard_theme

this_year = datetime.datetime.now().year
copyright_year = str(this_year) if this_year == 2020 else '2020-{0}'.format(this_year)

# -- Project information -----------------------------------------------------

project = 'MusicBrainz Picard'
# copyright = '{0}, MetaBrainz Foundation'.format(copyright_year)
copyright = '{0}, Bob Swift'.format(copyright_year)
author = 'Bob Swift'
# author = ''

# The full version, including alpha/beta/rc tags
release = 'v2.3.2'
version = release

# -- Notice for Back of Title Page in LaTex Output ---------------------------

# my_top_space = r'\vspace*{0.2\textheight}'
# my_sig_space = r'\vspace*{2.5em}'
# my_sep_space = r'\vspace*{\fill}'
# my_bot_space = r'\vspace{0.02\textheight}'

# my_notice = r'''{0}
# This document only exists because of the volunteer effort that
# went into its development, from the initial documentation on the Picard website,
# the information posted in the Community Discussion Forum, documentation from
# scripts, plugins and program source code, proofreaders, editors, translators,
# and feedback from the user community.\\
# \\
# My sincere thanks to all the volunteers for your time and effort that have
# helped make this documentation project a reality.\\

# {1}
# Bob Swift (rdswift)\\
# editor\\

# {2}
# Copyright © {4} Bob Swift (rdswift).\\
# Copyright © {4} MetaBrainz Foundation.\\
# \\
# Permission is granted to copy, distribute and/or modify this document under the
# terms of the GNU Free Documentation License, Version 1.3 or any later version
# published by the Free Software Foundation; with no Invariant Sections, no Front-
# Cover Texts, and no Back-Cover Texts. A copy of the license is available at
# https://www.gnu.org/licenses/fdl-1.3.html.
# {3}
# '''.format(my_top_space, my_sig_space, my_sep_space, my_bot_space, datetime.datetime.now().year,)

# my_notice = r'\vspace*{0.1\textheight}' + r'''
# This document only exists because of the volunteer effort that
# went into its development, from the initial documentation on the Picard website,
# the information posted in the Community Discussion Forum, documentation from
# scripts, plugins and program source code, proofreaders, editors, translators,
# and feedback from the user community.\\
# \\
# My sincere thanks to all the volunteers for your time and effort that have
# helped make this documentation project a reality.\\
# \vspace*{2.5em}

# Bob Swift (rdswift)\\
# editor\\

# ''' + r'\vspace*{\fill}' + r"""
# Copyright © {0} Bob Swift (rdswift).\\
# Copyright © {0} MetaBrainz Foundation.\\
# \\
# Permission is granted to copy, distribute and/or modify this document under the
# terms of the GNU Free Documentation License, Version 1.3 or any later version
# published by the Free Software Foundation; with no Invariant Sections, no Front-
# Cover Texts, and no Back-Cover Texts. A copy of the license is available at
# https://www.gnu.org/licenses/fdl-1.3.html.
# """.format(datetime.datetime.now().year,) + r'\vspace{0.1\textheight}'

# my_notice = r'''\vspace*{\fill}
# Copyright © 2020-''' + this_year + r''' Bob Swift\\
# Copyright © 2020-''' + this_year + r''' MetaBrainz Foundation\\
# \\
# Permission is granted to copy, distribute and/or modify this document under the
# terms of the GNU Free Documentation License, Version 1.3 or any later version
# published by the Free Software Foundation; with no Invariant Sections, no Front-
# Cover Texts, and no Back-Cover Texts. A copy of the license is available at
# https://www.gnu.org/licenses/fdl-1.3.html.
# \vspace{0.1\textheight}'''

my_notice = r'''\vspace*{\fill}
Copyright © ''' + copyright_year + r''' Bob Swift\\
\\
Permission is granted to copy, distribute and/or modify this document under the
terms of the GNU Free Documentation License, Version 1.3 or any later version
published by the Free Software Foundation; with no Invariant Sections, no Front-
Cover Texts, and no Back-Cover Texts. A copy of the license is available at
https://www.gnu.org/licenses/fdl-1.3.html.
\vspace{0.1\textheight}'''


# -- General configuration ---------------------------------------------------

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
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md', 'html', 'docs', 'locale', '.git', '.github', 'images', 'testing', 'README.md']


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
