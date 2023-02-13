from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "tasks"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="all"),
    path("task/<int:pk>/detail", views.TaskDetailView.as_view(), name="detail"),
    path("task/create/", views.TaskCreateView.as_view(), name="create"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="update"),
    path("task/<int:pk>/finish/", views.TaskFinishView.as_view(), name="finish"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="delete"),
    path(
        "category/create/", views.CategoryCreateView.as_view(), name="category-create"
    ),
    path("signup/", views.UserSignup.as_view(), name="signup"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="tasks:login"), name="logout"),
]
