from django import template
register=template.Library()
@register.filter(name='trunc')
def truncate_n(value,n):
    result=value[:n]
    return result