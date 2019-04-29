from django.urls import path, re_path
from main import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('time/', views.current_time),
    path('time/<int:pk>/', views.current_time_plus),
    #re_path(r'time/plus/(\d)/', views.current_time_plus),
]