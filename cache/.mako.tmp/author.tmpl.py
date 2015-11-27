# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448662153.4958003
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/author.tmpl'
_template_uri = 'author.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


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
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        parent = context.get('parent', UNDEFINED)
        author = context.get('author', UNDEFINED)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        generate_rss = context.get('generate_rss', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        description = context.get('description', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        author = context.get('author', UNDEFINED)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def content():
            return render_content(context)
        generate_rss = context.get('generate_rss', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        description = context.get('description', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="authorpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('        <p>')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('</p>\n')
        __M_writer('        <div class="metadata">\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('                <p class="feedlink">\n                    <a href="')
                __M_writer(str(_link(kind + "_rss", author, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="application/rss+xml">')
                __M_writer(str(messages('RSS feed', language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>&nbsp;\n                </p>\n')
        elif generate_rss:
            __M_writer('                <p class="feedlink"><a href="')
            __M_writer(str(_link(kind + "_rss", author)))
            __M_writer('" type="application/rss+xml">')
            __M_writer(str(messages('RSS feed')))
            __M_writer('</a></p>\n')
        __M_writer('        </div>\n    </header>\n')
        if posts:
            __M_writer('    <ul class="postlist">\n')
            for post in posts:
                __M_writer('        <li><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        author = context.get('author', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(filters.html_escape(str(author)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", author, language)))
                __M_writer('">\n')
        elif generate_rss:
            __M_writer('        <link rel="alternate" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(filters.html_escape(str(author)))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", author)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/author.tmpl", "source_encoding": "utf-8", "line_map": {"130": 4, "144": 4, "145": 5, "146": 5, "147": 6, "148": 7, "149": 8, "150": 8, "151": 8, "152": 8, "153": 8, "154": 8, "27": 0, "156": 8, "157": 8, "158": 10, "159": 11, "160": 11, "161": 11, "162": 11, "155": 8, "164": 11, "163": 11, "171": 165, "49": 2, "54": 13, "59": 43, "65": 16, "83": 16, "84": 19, "85": 19, "86": 20, "87": 21, "88": 21, "89": 21, "90": 23, "91": 24, "92": 25, "93": 26, "94": 27, "95": 27, "96": 27, "97": 27, "98": 27, "99": 27, "100": 27, "101": 27, "102": 30, "103": 31, "104": 31, "105": 31, "106": 31, "107": 31, "108": 33, "109": 35, "110": 36, "111": 37, "112": 38, "113": 38, "114": 38, "115": 38, "116": 38, "117": 38, "118": 38, "119": 38, "120": 38, "121": 38, "122": 38, "123": 40, "124": 42, "165": 11}, "uri": "author.tmpl"}
__M_END_METADATA
"""
