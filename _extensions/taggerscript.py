# -*- coding: utf-8 -*-
"""Sphinx extension to add a Picard Tagger Script lexer.
"""

from pygments.lexer import RegexLexer
from pygments.token import (
    Comment,
    Keyword,
    Name,
    String,
    Text,
)
from sphinx.application import Sphinx


class TaggerScriptLexer(RegexLexer):
    """Pygments lexer for Picard Tagger Script syntax.
    """
    name = 'Tagger script lexer'
    aliases = ['taggerscript']
    filenames = ['*.pts']

    tokens = {
        'root': [
            (r'[^\$%\\)]+', Text),
            (r'\\u[A-Fa-f0-9]{4}', String.Escape),
            (r'\\[^u]', String.Escape),
            (r'\$noop\(', Comment.Multiline, 'comment'),
            (r'\$[A-Za-z_0-9]+\(', Keyword),
            (r'%[A-Za-z_0-9:]+%', Name),
            (r'\)', Keyword),
        ],
        'comment': [
            (r'[^\$\\)]+', Comment.Multiline),
            (r'\\[()]', Comment.Multiline),
            (r'\$[A-Za-z_0-9]+\(', Comment.Multiline, '#push'),
            (r'\)', Comment.Multiline, '#pop'),
        ],
    }


def setup(sphinx: Sphinx):
    """Setup method to initialize this extension.
    """
    sphinx.add_lexer('taggerscript', TaggerScriptLexer)
