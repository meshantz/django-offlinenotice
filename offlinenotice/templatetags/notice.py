from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from offlinenotice.models import Notice


register = template.Library()


@register.simple_tag
def notice(slug):
    try:
        notice = Notice.objects.get(slug=slug)
    except (Notice.DoesNotExist, Notice.MultipleObjectsReturned), e:
        raise template.TemplateSyntaxError(
            _(u'Unable to load tag "%(slug)s".') % {'slug': slug,}
        )
    if notice.enabled:
        return notice.message_html
    else:
        return mark_safe(u'')


