from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TeamList.as_view(), name='list'),
]
