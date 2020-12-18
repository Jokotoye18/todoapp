from django.shortcuts import render, redirect, get_object_or_404
# from django.http import JsonResponse
# from django.core import serializers
from django.urls import reverse, reverse_lazy
from django.views.generic import View, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import TodoForm
from.models import Todo


class Todos(LoginRequiredMixin, View):
    login_url = "account_login"
    redirect_field_name = 'next'

    def get(self, *args, **kwargs):
        form = TodoForm()
        todo_list = Todo.objects.filter(owner__username=self.request.user.username).order_by("-id")
        context = {"form":form, "todo_list":todo_list}
        return render(self.request, "todo_list.html", context)

    def post(self, *args, **kwargs):
        form = TodoForm(self.request.POST or None)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = self.request.user
            todo.save()
            messages.success(self.request, 'Todo added successfully.')
            return redirect("todoapp:home")
        return render(self.request, "todo_list.html", {"form": form})
        

def delete_all( request):
    todos = Todo.objects.filter(owner__username=request.user.username)
    if request.method == 'POST':
        todos.delete()
        messages.success(request, 'You have successfully deleted all your todo.')
        return redirect("todoapp:home")
    return render(request, "delete_all.html") 

def delete_completed(request):
    todos = Todo.objects.filter(owner__username=request.user.username).filter(completed__exact=True)
    if request.method == 'POST':
        todos.delete()
        messages.success(request, 'You have successfully deleted all the completed todo.')
        return redirect("todoapp:home")
    context = {'todos':todos}
    return render(request, "delete_completed.html", context)

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo successfully deleted.')
        return redirect("todoapp:home")
    context = {'todo': todo}
    return render(request, "delete.html", context)


def mark_completed(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.completed = True
        todo.save()
        messages.info(request, 'successfully marked completed!')
        return redirect("todoapp:home")
    context = {'todo':todo}
    return render(request, 'mark_completed.html', context)

def mark_uncompleted(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.completed = False
        todo.save()
        messages.info(request, 'successfully marked uncompleted!')
        return redirect("todoapp:home")
    context = {'todo':todo}
    return render(request, 'mark_uncompleted.html', context)


