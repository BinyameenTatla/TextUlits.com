from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('removepunc/', views.removepunc, name='removepunc'),
    path('analyzed/', views.analyzed, name='analyzed'),
    path('ex1/', views.ex1, name='ex1'),
]