from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
@register.filter(is_safe=True)
def breaklines(x_times:int=1):
    br =""
    try:
        for i in range(x_times):
            br += "<br>"
    except: pass 
    return mark_safe(br)