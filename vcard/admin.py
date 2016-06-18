from django.contrib import admin
from . import models


class ProjectPictureInline(admin.TabularInline):
    model = models.ProjectPicture
    extra = 3
    ordering = ('order',)


class ProjectAdmin(admin.ModelAdmin):
    fields = ['caption', 'tag', 'url_name', 'description']
    list_display = ('caption',)
    inlines = [ProjectPictureInline]


class ContactInfoAdmin(admin.ModelAdmin):
    fields = ['text']
    list_display = ('text',)


class ProjectTagAdmin(admin.ModelAdmin):
    fields = ['caption', 'url_name']
    list_display = ('caption', 'url_name')



admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ContactInfo, ContactInfoAdmin)
admin.site.register(models.ProjectTag, ProjectTagAdmin)
