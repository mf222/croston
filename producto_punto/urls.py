from django.conf.urls import patterns, url  # , include


urlpatterns = patterns(
    'producto_punto.views',
    url(r'^$', 'home', name='home'),
    url(r'^process_data/$', 'process_data', name='pr_process_data'),
    url(r'^download_file/$', 'download_file', name='pr_download'),
)
