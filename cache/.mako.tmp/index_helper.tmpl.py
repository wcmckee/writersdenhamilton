# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448278322.9225297
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/index_helper.tmpl'
_template_uri = 'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if any(post.is_mathjax for post in posts):
            __M_writer('        <script type="text/javascript"\n          src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">\n        </script>\n        <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if prevlink or nextlink:
            __M_writer('        <nav class="postindexpager">\n        <ul class="pager">\n')
            if prevlink:
                __M_writer('            <li class="previous">\n                <a href="')
                __M_writer(str(prevlink))
                __M_writer('" rel="prev">')
                __M_writer(str(messages("Newer posts")))
                __M_writer('</a>\n            </li>\n')
            if nextlink:
                __M_writer('            <li class="next">\n                <a href="')
                __M_writer(str(nextlink))
                __M_writer('" rel="next">')
                __M_writer(str(messages("Older posts")))
                __M_writer('</a>\n            </li>\n')
            __M_writer('        </ul>\n        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/index_helper.tmpl", "uri": "index_helper.tmpl", "line_map": {"69": 63, "16": 0, "21": 19, "22": 30, "28": 21, "33": 21, "34": 22, "35": 23, "41": 2, "48": 2, "49": 3, "50": 4, "51": 6, "52": 7, "53": 8, "54": 8, "55": 8, "56": 8, "57": 11, "58": 12, "59": 13, "60": 13, "61": 13, "62": 13, "63": 16}}
__M_END_METADATA
"""
