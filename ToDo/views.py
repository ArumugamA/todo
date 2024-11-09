from django.shortcuts import render
from tasks.models import Task

def home(request):
    tasks = Task.objects.all().order_by('-updated_at')
    context = {'tasks': tasks}
    return render(request, 'home.html', context)