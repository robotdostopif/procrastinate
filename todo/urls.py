from django.urls import path
from . import views

app_name="todo"

urlpatterns = [
    path('', views.TaskListView.as_view(), name='all'),
    path('task/<int:pk>/detail', views.TaskDetailView.as_view(), name='detail'),
    path('task/create/', views.TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
]