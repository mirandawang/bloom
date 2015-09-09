from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^welcome/$', views.welcome),
    url(r'^create/$', views.create_plant),
    url(r'^play/myplant/(?P<plant_name>[\s0-9a-zA-Z]+)/customize/$', views.customize_plant),
    url(r'^play/myplant/(?P<plant_name>[\s0-9a-zA-Z]+)/$', views.play),
    url(r'^play/$', views.pick_plant),
    url(r'^friends/$', views.friends),
    url(r'^signup/$', views.create_user),
    url(r'^login/$', views.login_user),
    url(r'^logout/$', views.logout_user),
    url(r'^$', views.index),
]
