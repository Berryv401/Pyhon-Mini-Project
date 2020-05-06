from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.api.views import GymDetailsView, LocationDetailsView
from apps.api.views import GymListCreateView, LocationListCreateView

urlpatterns = {
    url(r'^gym-list/$', GymListCreateView.as_view(), name='gym-list'),
    url(r'^gym-update/(?P<pk>\d+)/$', GymDetailsView.as_view(), name='gym-update'),
    url(r'^location-list/$', LocationListCreateView.as_view(), name='location-list'),
    url(r'^student-update/(?P<pk>\d+)/$', LocationDetailsView.as_view(), name='location-update'),
}

urlpatterns = format_suffix_patterns(urlpatterns)