from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'qanda.views.home_page', name='home'),
    url(r'^questions/(.+)/$', 'qanda.views.view_question', name='question'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
