from django import template

register = template.Library()

@register.filter()
def to_int(value):
    try:
        return int(value)
    except:
        return value


@register.filter()
def visable(value, arg):
    if arg:
        return value.as_text()

@register.filter()
def add_classes(value, args):
    if args:
        return value.css_classes(args)