from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root URL for the homepage
    path('submit/', views.data, name='submit'),  # URL for form submission 
    path('db/', views.view, name='db'),  # URL for viewing the database
    path('delete/', views.delete, name='delete'),
    path('form/', views.form, name='form')
    ]
