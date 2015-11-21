# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1448068871.3135073
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/bootstrap/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_stylesheets', 'late_load_js', 'html_feedlinks', 'html_navigation_links', 'html_headstart', 'html_translations']


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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
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


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        colorbox_locales = _import_ns.get('colorbox_locales', context.get('colorbox_locales', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
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


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        generate_rss = _import_ns.get('generate_rss', context.get('generate_rss', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        rss_link = _import_ns.get('rss_link', context.get('rss_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        generate_atom = _import_ns.get('generate_atom', context.get('generate_atom', UNDEFINED))
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


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
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


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        twitter_card = _import_ns.get('twitter_card', context.get('twitter_card', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        use_open_graph = _import_ns.get('use_open_graph', context.get('use_open_graph', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        mathjax_config = _import_ns.get('mathjax_config', context.get('mathjax_config', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        striphtml = _import_ns.get('striphtml', context.get('striphtml', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        def html_feedlinks():
            return render_html_feedlinks(context)
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
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


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
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
{"line_map": {"23": 3, "26": 0, "33": 2, "34": 3, "35": 66, "36": 94, "37": 129, "38": 153, "39": 176, "40": 184, "46": 97, "59": 97, "60": 98, "61": 99, "62": 100, "63": 102, "64": 103, "65": 105, "66": 106, "67": 107, "68": 108, "69": 109, "70": 112, "71": 116, "72": 117, "73": 120, "74": 121, "75": 124, "76": 125, "77": 125, "78": 125, "79": 126, "80": 127, "81": 127, "82": 127, "88": 69, "99": 69, "100": 70, "101": 71, "102": 72, "103": 75, "104": 76, "105": 78, "106": 79, "107": 80, "108": 82, "109": 83, "110": 88, "111": 90, "112": 91, "113": 91, "114": 91, "115": 93, "116": 93, "117": 93, "123": 155, "135": 155, "136": 156, "137": 157, "138": 157, "139": 157, "140": 158, "141": 159, "142": 160, "143": 161, "144": 161, "145": 161, "146": 161, "147": 161, "148": 163, "149": 164, "150": 164, "151": 164, "152": 167, "153": 168, "154": 169, "155": 170, "156": 170, "157": 170, "158": 170, "159": 170, "160": 172, "161": 173, "162": 173, "163": 173, "169": 132, "182": 132, "183": 133, "184": 134, "185": 135, "186": 135, "187": 135, "188": 137, "189": 138, "190": 139, "191": 139, "192": 139, "193": 139, "194": 139, "195": 139, "196": 139, "197": 140, "198": 141, "199": 141, "200": 141, "201": 141, "202": 141, "203": 144, "204": 145, "205": 146, "206": 147, "207": 147, "208": 147, "209": 147, "210": 147, "211": 147, "212": 147, "213": 148, "214": 149, "215": 149, "216": 149, "217": 149, "218": 149, "224": 4, "253": 4, "254": 8, "255": 9, "256": 10, "257": 11, "258": 13, "259": 14, "260": 16, "261": 17, "262": 19, "263": 22, "264": 23, "265": 26, "266": 26, "267": 26, "268": 29, "269": 30, "270": 30, "271": 30, "272": 32, "273": 33, "274": 33, "275": 33, "276": 33, "277": 35, "278": 35, "279": 36, "280": 36, "281": 37, "282": 38, "283": 38, "284": 38, "285": 40, "286": 41, "287": 42, "288": 43, "289": 43, "290": 43, "291": 43, "292": 43, "293": 43, "294": 43, "295": 46, "296": 47, "297": 48, "298": 48, "299": 48, "300": 50, "301": 51, "302": 52, "303": 52, "304": 52, "305": 54, "306": 55, "307": 55, "308": 55, "309": 57, "310": 58, "311": 58, "312": 59, "313": 60, "314": 61, "315": 62, "316": 62, "317": 62, "318": 64, "319": 65, "320": 65, "326": 178, "337": 178, "338": 179, "339": 180, "340": 181, "341": 181, "342": 181, "343": 181, "344": 181, "345": 181, "346": 181, "352": 346}, "filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/bootstrap/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
