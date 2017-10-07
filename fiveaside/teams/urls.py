from django.conf.urls import url

from . import views

urlpatterns = [
    # Team List
    url(r'^$', views.TeamList.as_view(), name='list'),
    # Team Detail
    url(r'^(?P<pk>\d+)/$', views.TeamDetail.as_view(), name='detail'),
    # Team Create
    url(r'^create/$', views.TeamCreate.as_view(), name='create'),
    # Team Update
    url(r'^update/(?P<pk>\d+)', views.TeamUpdate.as_view(), name='update'),
    # Team Delete
    url(r'^delete/(?P<pk>\d+)/$', views.TeamDelete.as_view(), name='delete'),
]
