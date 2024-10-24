
# biblio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    
    path('member/<int:media_id>/', views.media_detail, name='member_detail'),
    path('members/create/', views.member_create, name='member_create'),
    path('members/<int:member_id>/update/', views.member_update, name='member_update'),
    path('members/<int:member_id>/delete/', views.member_delete, name='member_delete'),
    
    path('media/<int:media_id>/', views.media_detail, name='media_detail'),
    path('media/create/', views.media_create, name='media_create'),
    path('media/<int:media_id>/update/', views.media_update, name='media_update'),
    path('media/<int:media_id>/delete/', views.media_delete, name='media_delete'),
]
