from django.conf.urls import url

from . import views

urlpatterns = [
    # Team List
    url(r'^$', views.TeamList.as_view(), name='list'),
    # Team Detail
    url(r'^(?P<pk>\d+)/$', views.TeamDetail.as_view(), name='detail'),
]
