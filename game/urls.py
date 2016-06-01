from django.conf.urls import url
from django.contrib import admin
from gameapp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
    url(r'^ranking/$', views.ranking),
    url(r'^admin/', admin.site.urls),
]
