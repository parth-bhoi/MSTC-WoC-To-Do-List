from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task_date,Task_list
from .forms import home_form,view_task_form
import datetime

def index(request):
    x = home_form(request.POST)
    y = Task_date.objects.all()
    
    if x.is_valid():
        x.save()
    

    context = {
            'home_form' : home_form,
            'y' : y,
           
    }
    return render(request,'home.html' ,context)

def date_tasks(request, Task_date_id):

    z = view_task_form(request.POST)
    if z.is_valid():
        z.save()
    q = Task_date.objects.get(pk=Task_date_id)
    tasks = q.task_list_set.all()
    date = datetime.date.today()

    context = {
        'tasks' : tasks,
        'today_date':date,
        'q':q,
        'view_task_form':view_task_form
    }
    return render(request, 'view_task.html',context)

def about(request):
        return render(request, 'about.html',{})

def complete(request,Task_list_id,Task_date_id):
    task = Task_list.objects.get(id = Task_list_id)
    task.is_complete = True
    task.save()
    return redirect('date_tasks',Task_date_id = task.task_date_id)

def delcomplete(request,Task_date_id ):
    delobj = Task_list.objects.filter(is_complete = True)
    delobj.delete()
    return redirect('date_tasks',Task_date_id = Task_date_id)

def deleteone(request,Task_date_id,Task_list_id):
    task = Task_list.objects.get(id = Task_list_id)
    task.delete()
    return redirect('date_tasks',Task_date_id = Task_date_id)

def deldate(request, Task_date_id):
    date = Task_date.objects.get(id = Task_date_id)
    date.delete()
    return redirect('index')    

def delall(request, Task_date_id):
    task = Task_list.objects.get(task_date = Task_date_id)
    task.delete()
    return redirect('date_tasks',Task_date_id = Task_date_id)