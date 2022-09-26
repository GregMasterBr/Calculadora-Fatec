from atexit import register
from django import template
register = template.Library()
from datetime import date

@register.simple_tag(name='get_ano_calculadora')
def get_ano_calculadora():
    return date.today().year