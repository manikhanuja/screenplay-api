from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^screenplays/$', views.ScreenplayList.as_view()),
    url(r'^screenplays/(?P<pk>[0-9]+)$', views.ScreenplayListDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)