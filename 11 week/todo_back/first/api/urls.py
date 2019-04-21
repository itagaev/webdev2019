from django.urls import path
from api import views

urlpatterns = [
    path('api/task_lists/', views.task_lists),
    path('api/task_lists/<int:pk>/', views.task_lists_id),
    path('api/task_lists/<int:pk>/tasks', views.task_lists_id_tasks)
]