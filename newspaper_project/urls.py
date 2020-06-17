from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
