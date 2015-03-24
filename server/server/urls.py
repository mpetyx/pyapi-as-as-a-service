from django.conf.urls import patterns, include, url
from django.contrib import admin

from api import transform
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^transform/', transform, name='transform'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]