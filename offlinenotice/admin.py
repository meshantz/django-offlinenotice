from django.contrib import admin

from models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'enabled')
    list_editable = ('enabled',)
    prepopulated_fields = {"slug": ("title",)}
    exclude = [
        'message_html',
    ]

admin.site.register(Notice, NoticeAdmin)
