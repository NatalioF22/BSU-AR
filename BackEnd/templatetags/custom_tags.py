# templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter(name='get_attr')
def get_attribute(obj, attr_name):
    """Template filter to access object attributes dynamically"""
    return getattr(obj, attr_name, '')