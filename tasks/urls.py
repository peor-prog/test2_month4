from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
]