# This extension is based on the sphinxcontrib-inlinesyntaxhighlight
# By Kay-Uwe (Kiwi) Lorenz
#
# https://bitbucket.org/klorenz/sphinxcontrib-inlinesyntaxhighlight/
#
# Copyright (c) 2013, Kay-Uwe (Kiwi) Lorenz
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL "Kay-Uwe (Kiwi) Lorenz" BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re

from docutils import nodes

from sphinx.writers.html import HTMLTranslator

DIV_PRE_RE = re.compile(r'^<div[^>]*><pre>')
PRE_DIV_RE = re.compile(r'\s*</pre></div>\s*$')


def html_visit_literal(self, node):

    shall_highlight = False
    
    code_keyword = 'code' in node['classes']
    anyscript_keyword = any(
        v in [c.lower() for c in node['classes']]
        for v in ('anyscript', 'anyscriptdoc')
    )

    if node.rawsource.startswith('``') or code_keyword or anyscript_keyword:
        if anyscript_keyword:
            lang = 'AnyScriptDoc'
        else:
            lang = self.highlightlang

        highlight_args = node.get('highlight_args', {})

        # determine if shall_highlight
        shall_highlight = True

        attrs = node.attributes

        if 'role' in attrs:  # e.g. for :file:`...`
            shall_highlight = False

        elif 'code' in attrs['classes'] and (attrs.get('language') or lang):
            shall_highlight = True

        if not lang or lang == 'none':
            shall_highlight = False

    if shall_highlight:
        highlighted = self.highlighter.highlight_block(
            node.astext(), lang, location=node, **highlight_args)

        # highlighted comes as <div class="highlighted"><pre>...</pre></div>
        highlighted = DIV_PRE_RE.sub('', highlighted)
        highlighted = PRE_DIV_RE.sub('', highlighted)

        starttag = self.starttag(
            node, 'code', suffix='',
            CLASS='docutils literal highlight highlight-%s' % lang
        )
        self.body.append(starttag + highlighted + '</code>')

    else:
        starttag = (
            self.starttag(node, 'code', suffix='', CLASS='docutils literal') 
            + '<span class="pre">'
        )
        self.body.append(starttag + node.astext() + '</span></code>')

    raise nodes.SkipNode


def html_depart_literal(self, node):
    pass


HTMLTranslator.visit_literal = html_visit_literal
HTMLTranslator.depart_literal = html_depart_literal


def setup(app):
    pass