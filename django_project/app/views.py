from django.shortcuts import render, redirect
from .models import Container

from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from .form import MyUserCreationForm, ContainerForm
from django.db.models import Q


# Create your views here.

def main(request):
    return render(request, 'main.html')


def home(request):
    containers = Container.objects.all()
    user_info = request.user.__str__()
    context = {'containers': containers, 'user_info': user_info}
    return render(request, 'app/home.html', context, )


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'app/login_register.html', context)


def logout_page(request):
    logout(request)
    return redirect('main')


def register_page(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'app/login_register.html', {'form': form})


def create_container(request):
    form = ContainerForm(initial={'port': request.user.__str__()})
    containers = Container.objects.all()
    user_info = request.user.__str__()
    context = {'containers': containers, 'form': form, 'user_info': user_info}
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/container_form.html', context)


def delete_container(request, pk):
    containers = Container.objects.all()
    user_info = request.user.__str__()
    container = Container.objects.get(id=pk)
    if request.method == 'POST':
        container.delete()
        return redirect('home')
    context = {'containers': containers, 'user_info': user_info}
    return render(request, 'app/container_delete.html', context)


def update_container(request, pk):
    container = Container.objects.get(id=pk)
    form = ContainerForm(instance=container)
    user_info = request.user.__str__()
    containers = Container.objects.all()
    if request.method == 'POST':
        form = ContainerForm(request.POST, instance=container)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'containers': containers, 'user_info': user_info}
    return render(request, 'app/container_update.html', context)


def read_container(request, pk):
    container = Container.objects.get(id=pk)
    context = {'container': container}
    return render(request, 'app/container.html', context)
