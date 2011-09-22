from django.contrib.markup.templatetags.markup import restructuredtext
from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    enabled = models.BooleanField()
    message = models.TextField()
    message_html = models.TextField()

    def save(self, *args, **kwargs):
        self.message_html = restructuredtext(self.message)
        super(Notice, self).save(*args, **kwargs)

    def tag(self):
        return u'{%% %(tagname)s %(slug)s %%}' % {
            'slug': self.slug,
            'tagname': 'notice',
        }
