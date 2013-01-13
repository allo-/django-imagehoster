from django.conf.urls import patterns, include, url
import views
import settings

urlpatterns = patterns('',
    url(r'^$', views.file_list.as_view(), name='file_list'),
    url(r'^upload/$', views.upload, name='upload'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
