from django.contrib import admin
from rogue.webapp.models import *

#Register your models with the admin interface here
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'itemType', 'trustLevel', 'enabled')
admin.site.register(ContentItem,ContentItemAdmin)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('imageId','subject', 'platform', 'sender', 'content','installApp','needClick','fromFriend','trustLevel','enabled')
admin.site.register(SocialMedia,SocialMediaAdmin)

class EmailAdmin(admin.ModelAdmin):
    list_display = ('imageId', 'subject', 'address', 'sender', 'date', 'content', 'containsPoorGrammar', 'containsHtml', 'containsImage', 'trustLevel', 'enabled')
admin.site.register(Email,EmailAdmin)

class WebpageAdmin(admin.ModelAdmin):
    list_display = ('imageId', 'https', 'webAddress', 'title', 'content', 'containsPoorGrammar', 'containsImage', 'trustLevel', 'enabled')
admin.site.register(Webpage,WebpageAdmin)

class TrustDecisionAdmin(admin.ModelAdmin):
    list_display = ('user','decision')
admin.site.register(TrustDecision,TrustDecisionAdmin)