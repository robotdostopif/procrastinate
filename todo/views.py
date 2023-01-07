from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone

from todo.models import Task
from todo.forms import TaskForm

class TaskBaseView(View):
    model = Task
    success_url = reverse_lazy('todo:all')

class TaskListView(TaskBaseView, ListView, FormView):
    fields = "__all__"
    form_class = TaskForm

class TaskDetailView(TaskBaseView, DetailView):
    """View to list the details from one Task.
    Use the 'Task' variable in the template to access
    the specific Task here and in the Views below"""

class TaskCreateView(TaskBaseView, CreateView):
    form_class = TaskForm
    def form_valid(self, form):
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(TaskBaseView, UpdateView):
    form_class = TaskForm
    
class TaskUpdateView(TaskBaseView, UpdateView):
    form_class = TaskForm
    
# TODO: Restructure this to API in the future
class TaskFinishView(TaskBaseView):
    def post(self, request, *args, **kwargs):
        task = self.model.objects.get(id=kwargs.get('pk'))
        print("task", task)
        task.is_finished = True if task.is_finished == False else False
        task.finished_at = timezone.now()
        task.save()
        return HttpResponseRedirect(self.success_url)

class TaskDeleteView(TaskBaseView, DeleteView):
    """View to delete a Task"""
