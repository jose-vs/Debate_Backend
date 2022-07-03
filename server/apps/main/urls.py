from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('posts/', views.getPosts, name="notes"),

]
