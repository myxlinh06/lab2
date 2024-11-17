# Demo/urls.py
from django.contrib import admin
from django.urls import path, include

from Demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name='mainpage'),
    path('accounts/', include('accounts.urls')),
]
