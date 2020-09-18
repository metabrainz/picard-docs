# Configuration file for the Sphinx documentation builder.
# -*- blah_coding: utf-8 -*-
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
release_list = [
    'v2.3.2',
    'v2.4',
    'v2.4.1',
    'v2.4.2',
]
version = release

# Language information
default_language = 'en'
supported_languages = [
    ('en', 'English'),
    ('fr', 'Française'),
    # ('de', 'Deutsche'),
    # ('es', 'Española'),
]

# -- Notice for Back of Title Page in LaTex Output ---------------------------

notice_text = 'MusicBrainz Picard User Guide by Bob Swift is licensed under CC0 1.0. ' \
    + 'To view a copy of this license, visit https://creativecommons.org/publicdomain/zero/1.0'
my_notice = r'\vspace*{\fill}' + "\n" + notice_text + "\n" + r'\vspace{0.1\textheight}'


# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "notfound.extension",
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
    '_ignored',
    '_images',
    '_locale',
    '.DS_Store',
    '.git',
    '.github',
    'docs',
    'html',
    'README.md',
    'README.md',
    'testing',
    'Thumbs.db',
    'TODO.md',
]


# -- Options for Internationalization ----------------------------------------

language = default_language
locale_dirs = ['_locale']
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

# html_js_files = ['/version_links.js']

html_context = {
    'extra_css_files': [
        '_static/css/extra.css',
    ],
    'default_language': default_language,
    'supported_languages': supported_languages,
    'releases': release_list,
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

# epub_cover = ('_static/epub_cover.png', 'epub-cover.html')
# epub_cover = ('_static/epub_cover.png', '')

# epub_show_urls = 'inline'
epub_show_urls = 'footnote'
# epub_show_urls = 'no'

epub_use_index = True


# -- Options for custom 404 page --------------------------------------

# sphinx-notfound-page
# https://github.com/readthedocs/sphinx-notfound-page

notfound_title = 'Page Not Found'
notfound_text_1 = "We're sorry but we are unable to find the requested page. Please use the table " \
    + "of contents or the search box in the left-hand sidebar to locate your topic."
notfound_text_2 = "If you believe that you have received this message in error, please report it on " \
    + "the <a href='https://github.com/rdswift/picard-docs/issues/new/choose' " \
    + "target='_blank'>documentation project site</a>.  Thanks."
notfound_script = r'''
<script>
    var target_language = 'en';
    var target_version = 'latest';
    var src_host = window.location.hostname;
    var src_protocol = window.location.protocol;
    var src_path = window.location.pathname;
    var src_path_parts = src_path.split('/');
    var target_path = '';
    var target_url = src_protocol + '//' + src_host + '/en/latest/not_found.html';

    const re_language = /^[a-z][a-z](-[A-Z][A-Z])?$/;
    const re_version_1 = /^[0-9][0-9\.]*$/;
    const re_version_2 = /^(latest|stable)$/;
    const re_version_3 = /^v[0-9][0-9\.]*$/;

    function is_language(test_language) {
        if (test_language.search(re_language) < 0) {
            return false
        }
        target_language = test_language;
        return true;
    }

    function is_rtd_version(test_version) {
        return ((test_version.search(re_version_1) >= 0) || (test_version.search(re_version_2) >= 0));
    }

    function is_version(test_version) {
        if (test_version.search(re_version_3) < 0) {
            return false;
        }
        target_version = test_version.substring(1, 1000);
        return true;
    }

    function test_url() {
        var counter = 1;
        if ((is_language(src_path_parts[counter])) && (is_rtd_version(src_path_parts[counter + 1]))) {
            return true;
        }
        if (is_version(src_path_parts[counter])) {
            counter += 1;
        }
        if (counter < src_path_parts.length) {
            if (is_language(src_path_parts[counter])) {
                target_path += '/' + target_language + '/' + target_version;
                counter += 1;
                while (counter < src_path_parts.length) {
                    target_path += '/' + src_path_parts[counter];
                    counter += 1;
                }
                target_url = src_protocol + '//' + src_host + target_path;
                document.getElementById('content').innerHTML = '<p>The page may have been moved to <a href="' + target_url + '">' + target_url + '</a>.</p>';
                window.location.replace(target_url);
            }
        }
    }

    test_url();
</script>
'''
notfound_context = {
    'title': notfound_title,
    'body': "\n<h1>" + notfound_title + "</h1>\n<p>\n" + notfound_text_1 + "\n</p>\n<div id='content'></div>\n<p>\n" + notfound_text_2 + "\n</p>\n" + notfound_script,
}
