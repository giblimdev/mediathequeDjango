from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('biblio/', include('biblio.urls')),
    path('member/', include('member.urls')),

]
