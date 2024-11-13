from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, "New Task Added!")
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 6)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def index(request):
    context = {
        'index_text': "Welcome to the Index Page!"
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html', {'contact_info': 'Contact Information'})


def about(request):
    return render(request, 'about.html', {'about_info': 'About This App'})

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    messages.success(request, "Task Deleted!")

    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, "Task Edited!")
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')