from django.conf.urls import url
from showtrip.views import TripList, TripWaypointList

urlpatterns = [
    url(r'^$', TripList.as_view()),
    url(r'^trip/([0-9]+)/$', TripWaypointList.as_view()),
    #url(r'^$', views.trip_list, name='trip_list'),
    #url(r'^trip/(?P<pk>[0-9]+)/$', views.trip_detail, name='trip_detail'),
]