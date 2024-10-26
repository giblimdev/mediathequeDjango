
# biblio/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.base, name='base'),
    
    path('home/', views.home, name='home'),
    
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    path('member/create/', views.member_create, name='member_create'),
    path('member/<int:member_id>/update/', views.member_update, name='member_update'),
    path('member/<int:member_id>/delete/', views.member_delete, name='member_delete'),
    
    path('media/<int:media_id>/', views.media_detail, name='media_detail'),
    path('media/create/', views.media_create, name='media_create'),
    path('media/<int:media_id>/update/', views.media_update, name='media_update'),
    path('media/<int:media_id>/delete/', views.media_delete, name='media_delete'),
    
   
    path('borrowing/<int:borrowing_id>/', views.borrowing_detail, name='borrowing_detail'),
    path('borrowing/create/', views.borrowing_create, name='borrowing_create'),
    path('borrowing/<int:borrowing_id>/update/', views.borrowing_update, name='borrowing_update'),
   
]
