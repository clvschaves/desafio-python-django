from django.urls import re_path
from django.contrib import admin

from .views import shrink_url, redirect

urlpatterns = [
    re_path(r'^$', shrink_url, name='shrink_url'),
    re_path(r'^(?P<short>\w+)/$', redirect, name='redirect'),
]