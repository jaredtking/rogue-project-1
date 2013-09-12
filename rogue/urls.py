from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

# Django Rest
from rest_framework import routers
from rogue.webapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rogue.views.home', name='home'),
    # url(r'^rogue/', include('rogue.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # route requests for / to the home controller view
    url(r'^$', 'rogue.webapp.views.home'),
    # route requests to the /foo/* functoin to the foo controller view
    url(r'^foo/(?P<foo_bar>\d+)', 'rogue.webapp.views.foo'),
    # Django Rest
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #Ember file
 	url(r'^ember/$', 'rogue.webapp.views.emberhome'),

    #route requests to the /cItem/* function to the getContentItem controller view
url(r'^cItem/(?P<item_name>\w+)/$', 'rogue.webapp.views.getContentItem'),  
)

