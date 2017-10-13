from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'dundaslinks.views.home'),
    url(r'^about/$', 'dundaslinks.views.about'),
    url(r'^products/$', 'dundaslinks.views.products'),
    url(r'^order/$', 'dundaslinks.views.order'),
    url(r'^news/', include('news.urls')),
    url(r'^contact/', include('contact.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
