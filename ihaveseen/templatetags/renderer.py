from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

register = template.Library()


@register.simple_tag
def render_jsx(filename):
    cdn_host = settings.CDN_HOST
    script_code = '<script src="{cdn_host}/{filename}#{commit_hash}" charset="UTF-8"></script>'
    return mark_safe(script_code.format(cdn_host=cdn_host, filename=filename, commit_hash=settings.GIT_HASH))
