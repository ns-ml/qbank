from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'qanda.views.check_answer', name='view_question'),
    url(r'^(\d+)/answer$', 'qanda.views.view_answer', name='view_answer'),
)
