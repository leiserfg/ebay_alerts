from django import template

register = template.Library()


@register.simple_tag
def under(obj, attrib_name):
    return getattr(obj, attrib_name, '') or obj.get(attrib_name, '')
