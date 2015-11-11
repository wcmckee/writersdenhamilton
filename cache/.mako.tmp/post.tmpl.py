# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1447234780.3454494
_enable_loop = True
_template_filename = 'themes/monospace/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n    <div class="post">\n    ')
        __M_writer(str(pheader.html_title()))
        __M_writer('\n        <div class="meta" style="background-color: rgb(234, 234, 234); ">\n        <span class="authordate">\n            ')
        __M_writer(str(messages("Posted:")))
        __M_writer(' <time class="published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\n')
        if not post.meta('password'):
            __M_writer('               [<a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>]\n')
        __M_writer('        </span>\n        <br>\n')
        if post.tags:
            __M_writer('                <span class="tags">')
            __M_writer(str(messages("Tags")))
            __M_writer(':&nbsp;\n')
            for tag in post.tags:
                __M_writer('                    <a class="tag" href="')
                __M_writer(str(_link('tag', tag)))
                __M_writer('"><span>')
                __M_writer(str(tag))
                __M_writer('</span></a>\n')
            __M_writer('                </span>\n                <br>\n')
        __M_writer('        <span class="authordate">\n            ')
        __M_writer(str(pheader.html_translations(post)))
        __M_writer('\n        </span>\n        </div>\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments'):
            __M_writer('        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\n')
        __M_writer('    ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "themes/monospace/templates/post.tmpl", "uri": "post.tmpl", "line_map": {"129": 6, "137": 6, "138": 7, "139": 7, "140": 8, "141": 9, "142": 9, "143": 9, "149": 143, "23": 4, "26": 3, "29": 2, "35": 0, "51": 2, "52": 3, "53": 4, "54": 5, "59": 11, "64": 42, "70": 12, "83": 12, "84": 14, "85": 14, "86": 17, "87": 17, "88": 17, "89": 17, "90": 17, "91": 17, "92": 18, "93": 19, "94": 19, "95": 19, "96": 19, "97": 19, "98": 21, "99": 23, "100": 24, "101": 24, "102": 24, "103": 25, "104": 26, "105": 26, "106": 26, "107": 26, "108": 26, "109": 28, "110": 31, "111": 32, "112": 32, "113": 35, "114": 35, "115": 36, "116": 36, "117": 37, "118": 38, "119": 38, "120": 38, "121": 40, "122": 40, "123": 40}}
__M_END_METADATA
"""
