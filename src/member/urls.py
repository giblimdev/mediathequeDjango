from django.urls import path
from .views import maliste

urlpatterns=[
path('',maliste , name='list-media')]