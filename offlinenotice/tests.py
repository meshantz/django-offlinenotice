"""
Tests for OfflineNotice
"""

from django.test import TestCase
from django.template import Template, Context, TemplateSyntaxError

from models import Notice


class NoticeTagTest(TestCase):
    fixtures = ['testnotices',]

    def test_enabled_tag(self):
        template = Template('{% load notice %}{% notice "testable" %}')
        rendered = template.render(Context({}))
        notice = Notice.objects.get(slug='testable')
        self.assertEqual(rendered, notice.message_html)

    def test_disabled_tag(self):
        template = Template('{% load notice %}{% notice "diabledtest" %}')
        rendered = template.render(Context({}))
        self.assertEqual(rendered, u'')

    def test_unknown_tag(self):
        template = Template('{% load notice %}{% notice "never-was" %}')
        self.assertRaises(TemplateSyntaxError, template.render, Context({}))

