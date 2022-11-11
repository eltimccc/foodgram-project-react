from django.contrib import admin

from .models import Tags

class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color',)
    list_filter = ('slug',)
    search_fields = ('slug',)

admin.site.register(Tags, TagsAdmin)