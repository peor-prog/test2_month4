from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task


def task_list(request):
  tasks = Task.objects.all()
  form = TaskForm()

  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('task_list')

  context = {'tasks': tasks, 'form': form}
  return render(request, 'tasks/task_list.html', context)


def task_detail(request, pk):
  task = get_object_or_404(Task, pk=pk)
  return render(request, 'tasks/task_detail.html', {'task': task})


def toggle_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.completed = not task.completed
  task.save()
  return redirect('task_list')