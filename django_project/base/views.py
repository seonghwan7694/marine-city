from django.shortcuts import render,redirect
from .models import Container
from .form import ContainerForm

from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    containers = Container.objects.all()
    context = {'containers': containers}
    return render(request, 'base/home.html', context)

def read_container(request, pk):
    container = Container.objects.get(id=pk)
    context = {'container': container}
    return render(request, 'base/container.html', context)

def create_container(request):
    form = ContainerForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/container_form.html', context)

def update_container(request, pk):
    container = Container.objects.get(id=pk)
    form = ContainerForm(instance=container)
    if request.method == 'POST':
        form = ContainerForm(request.POST, instance=container)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/container_form.html', context)

def delete_container(request, pk):
    container = Container.objects.get(id=pk)
    if request.method == 'POST':
        container.delete()
        return redirect('home')
    return render(request, 'base/container_delete.html', {'obj':container})