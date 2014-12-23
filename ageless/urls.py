import os
#from django.conf.urls.defaults import *

from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ageless.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'inandout.views.home', name='home'),
    # url(r'^inandout/', include('inandout.urls')),
    url(r'^$', include('inandout.urls')),

    url(r'^product/', include('inandout.urls')),
    url(r'^blog/', include('inandout.urls')),
    url(r'^testamonial/', include('inandout.urls')),

    url(r'^contact_us/', 'inandout.views.contact_us', name='contact_us'),
    url(r'^about_us/', 'inandout.views.about_us', name='about_us'),

    url(r'^gplus_login/', 'inandout.views.gplus_login', name='gplus_login'),
    url(r'^user_logout/', 'inandout.views.user_logout', name='user_logout'),




    url(r'^plustest/', 'inandout.views.index'),
    url(r'^oauth2callback/', 'inandout.views.auth_return'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'inandout/login.html'}
                        ),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'static')
}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
