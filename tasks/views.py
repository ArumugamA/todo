from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
# Create your views here.

def addtask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def markasdone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markasundone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edittask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('home')
    else:
        context = {'task': task}
    
    return render(request, 'edittask.html', context)

def deletetask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')