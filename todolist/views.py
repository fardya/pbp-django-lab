import datetime
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user= request.user)
    context = {
        'list_todo': data_todolist
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Wrong username or password')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

class TaskForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(title=form.cleaned_data["title"], description=form.cleaned_data["description"], date=datetime.datetime.now(), user=request.user)
            return HttpResponseRedirect(reverse('todolist:show_todolist'))
    else:
        form = TaskForm()
    
    context = {'form':form}
    return render(request, 'create-task.html', context)

@login_required(login_url='/todolist/login/')
def status(request, id):
    todo = Task.objects.get(id=id, user=request.user)
    todo.is_finished = not todo.is_finished
    todo.save(update_fields=['is_finished'])
    return HttpResponseRedirect(reverse('todolist:show_todolist'))
    # return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete(request, id):
    Task.objects.get(id=id).delete()
    return redirect('todolist:show_todolist')
