from django.conf.urls import patterns, url  # , include
from . import views


urlpatterns = patterns(
    'producto_punto.views',
    url(r'^$', views.UploadView.as_view(), name='home'),
    url(r'^download_file/$', 'download_file', name='pr_download'),
)
