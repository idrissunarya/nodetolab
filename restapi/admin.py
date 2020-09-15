from django.contrib import admin
from .models import Tag

class TagModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    class Meta:
        model = Tag
admin.site.register(Tag, TagModelAdmin)

