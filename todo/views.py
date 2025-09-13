from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task, is_completed=False)
    return HttpResponse("Add Task")
