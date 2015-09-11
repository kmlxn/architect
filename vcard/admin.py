from django.contrib import admin
from . import models



class ProjectAdmin(admin.ModelAdmin):
    fields = ['picture', 'caption']
    list_display = ('caption', 'picture')



class ContactInfoAdmin(admin.ModelAdmin):
    fields = ['text']
    list_display = ('text',)



class TextOnSiteAdmin(admin.ModelAdmin):
    fields = ['name', 'text']
    list_display = ('name', 'text')



admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ContactInfo, ContactInfoAdmin)
admin.site.register(models.TextOnSite, TextOnSiteAdmin)
