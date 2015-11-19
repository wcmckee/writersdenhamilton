# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1447893631.7101598
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/bootstrap/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'html_feedlinks', 'late_load_js', 'html_stylesheets', 'html_navigation_links', 'html_translations']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        def html_feedlinks():
            return render_html_feedlinks(context)
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        use_open_graph = _import_ns.get('use_open_graph', context.get('use_open_graph', UNDEFINED))
        striphtml = _import_ns.get('striphtml', context.get('striphtml', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        twitter_card = _import_ns.get('twitter_card', context.get('twitter_card', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        mathjax_config = _import_ns.get('mathjax_config', context.get('mathjax_config', UNDEFINED))
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        generate_rss = _import_ns.get('generate_rss', context.get('generate_rss', UNDEFINED))
        generate_atom = _import_ns.get('generate_atom', context.get('generate_atom', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        rss_link = _import_ns.get('rss_link', context.get('rss_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        colorbox_locales = _import_ns.get('colorbox_locales', context.get('colorbox_locales', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            __M_writer('        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        if colorbox_locales[lang]:
            __M_writer('        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(str(colorbox_locales[lang]))
            __M_writer('.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="//maxcdn.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer('            <link href="//maxcdn.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">\n')
            else:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n            <link href="/assets/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">')
                __M_writer(str(text))
                __M_writer('<b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"23": 3, "26": 0, "33": 2, "34": 3, "35": 66, "36": 94, "37": 129, "38": 153, "39": 176, "40": 184, "46": 4, "75": 4, "76": 8, "77": 9, "78": 10, "79": 11, "80": 13, "81": 14, "82": 16, "83": 17, "84": 19, "85": 22, "86": 23, "87": 26, "88": 26, "89": 26, "90": 29, "91": 30, "92": 30, "93": 30, "94": 32, "95": 33, "96": 33, "97": 33, "98": 33, "99": 35, "100": 35, "101": 36, "102": 36, "103": 37, "104": 38, "105": 38, "106": 38, "107": 40, "108": 41, "109": 42, "110": 43, "111": 43, "112": 43, "113": 43, "114": 43, "115": 43, "116": 43, "117": 46, "118": 47, "119": 48, "120": 48, "121": 48, "122": 50, "123": 51, "124": 52, "125": 52, "126": 52, "127": 54, "128": 55, "129": 55, "130": 55, "131": 57, "132": 58, "133": 58, "134": 59, "135": 60, "136": 61, "137": 62, "138": 62, "139": 62, "140": 64, "141": 65, "142": 65, "148": 155, "160": 155, "161": 156, "162": 157, "163": 157, "164": 157, "165": 158, "166": 159, "167": 160, "168": 161, "169": 161, "170": 161, "171": 161, "172": 161, "173": 163, "174": 164, "175": 164, "176": 164, "177": 167, "178": 168, "179": 169, "180": 170, "181": 170, "182": 170, "183": 170, "184": 170, "185": 172, "186": 173, "187": 173, "188": 173, "194": 69, "205": 69, "206": 70, "207": 71, "208": 72, "209": 75, "210": 76, "211": 78, "212": 79, "213": 80, "214": 82, "215": 83, "216": 88, "217": 90, "218": 91, "219": 91, "220": 91, "221": 93, "222": 93, "223": 93, "229": 97, "242": 97, "243": 98, "244": 99, "245": 100, "246": 102, "247": 103, "248": 105, "249": 106, "250": 107, "251": 108, "252": 109, "253": 112, "254": 116, "255": 117, "256": 120, "257": 121, "258": 124, "259": 125, "260": 125, "261": 125, "262": 126, "263": 127, "264": 127, "265": 127, "271": 132, "284": 132, "285": 133, "286": 134, "287": 135, "288": 135, "289": 135, "290": 137, "291": 138, "292": 139, "293": 139, "294": 139, "295": 139, "296": 139, "297": 139, "298": 139, "299": 140, "300": 141, "301": 141, "302": 141, "303": 141, "304": 141, "305": 144, "306": 145, "307": 146, "308": 147, "309": 147, "310": 147, "311": 147, "312": 147, "313": 147, "314": 147, "315": 148, "316": 149, "317": 149, "318": 149, "319": 149, "320": 149, "326": 178, "337": 178, "338": 179, "339": 180, "340": 181, "341": 181, "342": 181, "343": 181, "344": 181, "345": 181, "346": 181, "352": 346}, "source_encoding": "utf-8", "uri": "base_helper.tmpl", "filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/bootstrap/templates/base_helper.tmpl"}
__M_END_METADATA
"""
