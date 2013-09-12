from django.contrib import admin
from rogue.webapp.models import *

#Register your models with the admin interface here
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'itemType', 'trustLevel', 'enabled')
admin.site.register(ContentItem,ContentItemAdmin)