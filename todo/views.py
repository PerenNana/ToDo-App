from django.shortcuts import render, get_object_or_404, redirect
from .models import Task


def addTask(request):
    task = request.POST['task']
    new_task = Task.objects.create(task=task, is_completed=False)
    new_task.description = task
    new_task.save()
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        new_task_priority = request.POST['priority']
        new_task_description = request.POST.get('description', '')
        new_task_deadline = request.POST.get('deadline', '')

        task.task = new_task
        task.priority = new_task_priority
        task.description = new_task_description
        task.deadline = new_task_deadline
        task.save()
        return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')