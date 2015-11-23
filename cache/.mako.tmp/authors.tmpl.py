# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448264528.1668437
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/bootstrap3/templates/authors.tmpl'
_template_uri = 'authors.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        hidden_authors = context.get('hidden_authors', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        hidden_authors = context.get('hidden_authors', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if items:
            __M_writer('    <h2>')
            __M_writer(str(messages("Authors")))
            __M_writer('</h2>\n')
        if items:
            __M_writer('    <ul class="list-inline">\n')
            for text, link in items:
                if text not in hidden_authors:
                    __M_writer('            <li><a class="reference badge" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 10, "65": 11, "66": 12, "27": 0, "68": 12, "37": 2, "70": 12, "71": 15, "42": 17, "77": 71, "48": 4, "67": 12, "69": 12, "57": 4, "58": 5, "59": 6, "60": 6, "61": 6, "62": 8, "63": 9}, "filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/bootstrap3/templates/authors.tmpl", "source_encoding": "utf-8", "uri": "authors.tmpl"}
__M_END_METADATA
"""
