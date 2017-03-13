from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from superheroes import views

urlpatterns = [
    url(r'^superheroe/$', views.SuperHeroeList.as_view()),
    url(r'^superheroe/(?P<pk>[0-9]+)/$', views.SuperHeroeDetail.as_view()),
    url(r'^publisher/$', views.PublisherList.as_view()),
    url(r'^publisher/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
