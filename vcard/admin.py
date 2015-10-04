from django.contrib import admin
from . import models



class ProjectAdmin(admin.ModelAdmin):
    fields = ['picture', 'caption', 'tag']
    list_display = ('caption', 'picture')



class ContactInfoAdmin(admin.ModelAdmin):
    fields = ['text']
    list_display = ('text',)



class TextOnSiteAdmin(admin.ModelAdmin):
    fields = ['name', 'text']
    list_display = ('name', 'text')



class ProjectTagAdmin(admin.ModelAdmin):
    fields = ['caption', 'alias']
    list_display = ('caption', 'alias')



admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ContactInfo, ContactInfoAdmin)
admin.site.register(models.TextOnSite, TextOnSiteAdmin)
admin.site.register(models.ProjectTag, ProjectTagAdmin)
