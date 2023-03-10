from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db import transaction
from django.http import HttpResponseRedirect
from django.utils import timezone
from rest_framework import viewsets
from django.shortcuts import render

from tasks.models import Category, AppUser, Task
from tasks.forms import CategoryForm, TaskForm, UserSignInForm, UserSignUpForm

from django.views.generic.edit import FormView
from tasks.serializers import TaskSerializer, CategorySerializer


class UserSignup(CreateView):
    template_name = "tasks/signup.html"
    form_class = UserSignUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks:login")

    def form_valid(self, form):
        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                AppUser.objects.create(user=user, name=user.username)
        else:
            print(form.errors)
        return super(UserSignup, self).form_valid(form)


class UserLogin(LoginView):
    template_name = "tasks/signin.html"
    fields = "__all__"
    redirect_authenticated_user = True
    form_class = UserSignInForm

    def get_success_url(self):
        return reverse_lazy("tasks:all")


class TaskBaseView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("tasks:all")


class TaskListView(TaskBaseView, ListView, FormView):
    fields = "__all__"
    form_class = TaskForm

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(app_user__user=self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(TaskListView, self).get_context_data(*args, **kwargs)
        context["category_form"] = CategoryForm()
        return context


class TaskDetailView(TaskBaseView, DetailView):
    """View to list the details from one Task.
    Use the 'Task' variable in the template to access
    the specific Task here and in the Views below"""


class TaskCreateView(TaskBaseView, CreateView):
    form_class = TaskForm

    def form_valid(self, form):
        if form.is_valid():
            form.instance.app_user = AppUser.objects.get(user=self.request.user)
            form.save()
        else:
            print(form.errors)
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(TaskBaseView, UpdateView):
    form_class = TaskForm

    def form_valid(self, form):
        if form.is_valid():
            form.instance.app_user = AppUser.objects.get(user=self.request.user)
            form.save()
        else:
            print(form.errors)
        return super(TaskUpdateView, self).form_valid(form)


# TODO: Restructure this to API in the future
class TaskFinishView(TaskBaseView):
    def post(self, request, *args, **kwargs):
        task = self.model.objects.get(id=kwargs.get("pk"))
        task.is_finished = True if task.is_finished == False else False
        task.finished_at = timezone.now()
        task.save()
        return HttpResponseRedirect(self.success_url)


class TaskDeleteView(TaskBaseView, DeleteView):
    """View to delete a Task"""


class CategoryBaseView(LoginRequiredMixin, View):
    model = Category
    success_url = reverse_lazy("tasks:all")
    fields = "__all__"


class CategoryCreateView(CategoryBaseView, CreateView):
    def form_valid(self, form):
        if form.is_valid():
            form.instance.app_user = AppUser.objects.get(user=self.request.user)
            form.save()
        else:
            print(form.errors)
        return super(CategoryCreateView, self).form_valid(form)


class TaskView(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class CategoryView(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
