from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'qanda.views.home_page', name='home'),
    url(r'^questions/(\d+)/$', 'qanda.views.check_answer', name='question'),
    url(r'^questions/(\d+)/answer$', 'qanda.views.view_answer', name='answer'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
