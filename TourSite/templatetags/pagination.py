import urllib.parse

from django import template
from django.core.handlers.wsgi import WSGIRequest

register = template.Library()


@register.simple_tag
def get_page_url(request: WSGIRequest, new_key: str, new_val: str):
    queries = {key: val for key, val in request.GET.items()}
    queries[new_key] = new_val
    query_string = urllib.parse.urlencode(queries)
    return "?" + query_string
