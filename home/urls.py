from django.urls import path,include, re_path
# from django.conf.urls import url
from home.views import *
from car_owner_portal import *
from customer_portal import *

urlpatterns = [
    re_path(r'^$',home_page),
]
