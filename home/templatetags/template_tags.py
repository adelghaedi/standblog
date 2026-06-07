from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag
def current_date(format_string):
    return datetime.now().strftime(format_string)


@register.inclusion_tag(filename="home/recent_articles.html")
def recent_articles_tag(recent_articles):
    return {"recent_articles": recent_articles}



