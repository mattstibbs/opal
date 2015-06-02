"""
Templatetags for including OPAL plugins
"""
from django import template

from opal.core import application, plugins

register = template.Library()

@register.inclusion_tag('plugins/javascripts.html')
def plugin_javascripts(namespace):
    def scripts():
        for plugin in plugins.plugins():
            if namespace in plugin.javascripts:
                for javascript in plugin.javascripts[namespace]:
                    yield javascript
    return dict(javascripts=scripts)

@register.inclusion_tag('plugins/stylesheets.html')
def plugin_stylesheets():
    def styles():
        for plugin in plugins.plugins():
            for sheet in plugin.stylesheets:
                yield sheet
    return dict(styles=styles)

@register.inclusion_tag('plugins/head_extra.html', takes_context=True)
def plugin_head_extra(context):
    def templates():
        for plugin in plugins.plugins():
            for tpl in plugin.head_extra:
                    yield tpl
    ctx = context
    ctx['head_extra'] = templates
    return ctx

@register.inclusion_tag('plugins/menuitems.html')
def plugin_menuitems():
    def items():
        for plugin in plugins.plugins():
            for i in plugin.menuitems:
                yield i
    return dict(items=items)

@register.inclusion_tag('plugins/menuitems.html')
def application_menuitems():
    def items():
        app = application.get_app()
        for i in app.menuitems:
            yield i
    return dict(items=items)
    
@register.inclusion_tag('plugins/angular_module_deps.html')
def plugin_opal_angular_deps():
    def deps():
        for plugin in plugins.plugins():
            for i in plugin.angular_module_deps:
                yield i
    return dict(deps=deps)

@register.inclusion_tag('plugins/javascripts.html')
def core_javascripts(namespace):
    def scripts():
        app = application.get_app()
        for javascript in app.core_javascripts[namespace]:
            yield javascript
    return dict(javascripts=scripts)

@register.inclusion_tag('plugins/javascripts.html')
def application_javascripts():
    def scripts():
        app = application.get_app()
        for javascript in app.javascripts:
            yield javascript
    return dict(javascripts=scripts)

@register.inclusion_tag('plugins/actions.html')
def application_actions():
    def actions():
        app = application.get_app()
        for action in app.actions:
            yield action
        for plugin in plugins.plugins():
            for action in plugin.actions:
                yield action
    return dict(actions=actions)
