from django import template

register = template.Library()

def cut(value, arg):
    """
    doc string
    """
    return value.replace(arg, '')

register.filter('cut', cut)
