from django.urls import re_path
from dscan import views

app_name = 'dscan'

urlpatterns = [
    re_path(r'^$', views.landing, name="landing"),
    re_path(r'^parse', views.parse, name="parse"),
    re_path(r'^about', views.about, name="about"),
    re_path(r'^(?P<token>.*)$', views.show, name="show")
]