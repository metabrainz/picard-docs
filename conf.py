# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# pylint: disable=missing-module-docstring


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import datetime
import re

# import sphinx_rtd_theme
# import picard_theme

this_year = datetime.datetime.now().year
copyright_year = str(this_year) if this_year == 2020 else '2020-{0}'.format(this_year)

# -- Project information -----------------------------------------------------

project = 'MusicBrainz Picard'

# The full version, including alpha/beta/rc tags (must start with a 'v' and not contain any spaces)
version = 'v2.6.2'

author = 'Bob Swift'
# copyright = 'MusicBrainz Picard User Guide by Bob Swift is licensed under CC0 1.0. To view a copy of this license, visit https://creativecommons.org/publicdomain/zero/1.0'
copyright = 'This documentation is licensed under CC0 1.0.'     # pylint: disable=redefined-builtin

# -- Language information ----------------------------------------------------

default_language = 'en'
supported_languages = [
    ('en', 'English'),
    ('fr', 'Français'),
    # ('de', 'Deutsch'),
    # ('es', 'Español'),
]

# -- Base file name for PDF and EPUB files -----------------------------------

base_filename = 'musicbrainzpicard'


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
    '_images',
    '_ignored',
    '_locale',
    'Thumbs.db',
    '.DS_Store',
    'README.md',
    'html',
    'docs',
    '.git',
    '.github',
    'images',
    'testing',
    'README.md',
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

html_js_files = ['/version_links.js']

# Major.minor portion of the version number used for naming the download files
major_minor = re.match(r'^(v[0-9]+\.[0-9]+)', version).group(1)

html_context = {
    'extra_css_files': [
        '_static/css/extra.css',
    ],
    'default_language': default_language,
    'supported_languages': supported_languages,
    'major_minor': major_minor,
    'release': version,
}

html_favicon = '_static/picard-icon.png'

html_copy_source = False


# -- Options for LaTeX / PDF output ------------------------------------------

release = version   # For display on cover of PDF document

latex_documents = [
    ('pdf', '{0}.tex'.format(base_filename), project, '', 'manual', False),
    # ('pdf', '{0}.tex'.format(base_filename), project, 'Edited by Bob Swift', 'manual', False),
    # ('pdf', '{0}.tex'.format(base_filename), project, '', 'howto', False),
]

# latex_toplevel_sectioning = 'part'
# latex_toplevel_sectioning = 'section'     # Use with 'howto' document style
# latex_toplevel_sectioning = 'chapter'

# latex_show_urls = 'inline'
# latex_show_urls = 'footnote'
latex_show_urls = 'no'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    # 'preamble': '\\hyphenation{Music-Brainz}',
    'preamble': r'''\hyphenation{Music-Brainz}
\usepackage{fontspec}
\setmainfont{DejaVu Sans}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
\newcommand\sphinxbackoftitlepage{''' + my_notice + r'''}
''',
    'extraclassoptions': 'openany',
    # 'maketitle': r'\newcommand\sphinxbackoftitlepage{<Extra material>}\sphinxmaketitle',
    # 'maketitle': r'\newcommand\sphinxbackoftitlepage{<Extra material>}\sphinxmaketitle',
}

latex_domain_indices = True


# -- Options for epub output ------------------------------------------

epub_basename = base_filename

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

notfound_template = 'custom_404.html'
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
