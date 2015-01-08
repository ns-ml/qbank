from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'qanda.views.home_page', name='home'),
    url(r'^questions/(\d+)/$', 'qanda.views.check_answer', name='view_question'),
    url(r'^questions/(\d+)/answer$', 'qanda.views.view_answer', name='view_answer'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'qanda.views.register', name='register'),
)
