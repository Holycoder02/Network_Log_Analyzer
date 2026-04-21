from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_log, name='upload_log'),
    path('dashboard/', views.dashboard, name='dashboard'),
]