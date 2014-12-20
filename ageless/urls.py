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


)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
