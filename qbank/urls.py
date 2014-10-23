from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'qanda.views.home_page', name='home'),
    url(r'^questions/', include('qanda.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
