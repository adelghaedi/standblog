from django import template

register = template.Library()


def cutter(value, arg):
    return f"{value[:arg]}..."


register.filter(name="cutter", filter_func=cutter)


