from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'moviepicker.views.home', name='home'),
    url(r'^(?P<username>)/$', 'moviepicker.views.watcher_details', name='watcher_details'),

    url(r'^get-results/$', 'moviepicker.views.get_results', name='get_results'),
    url(r'^(?P<username>)/votes/$', 'moviepicker.views.watcher_votes', name='watcher_votes'),

    url(r'^vote-toggle/$', 'moviepicker.views.vote_toggle', name='vote_toggle'),
]
