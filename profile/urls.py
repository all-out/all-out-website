from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'profile.views.login', name='login'),
    url(r'^logout/$', 'profile.views.logout', name='logout'),
]
