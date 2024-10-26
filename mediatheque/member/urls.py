from django.urls import path
from .views import list_media

urlpatterns=[
path('', list_media , name='list-media')]