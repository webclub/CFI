from django.conf.urls import include, url
from django.contrib import admin

from food.views import *

urlpatterns = [
    url(r'^reg_kitchen/', register_kitchen),
    url(r'^reg_school/', register_school),
    url(r'^reg_teacher/', register_teacher),
    url(r'^reg_manager/', register_manager),
    url(r'^update_attendance/', update_attendance),
]
