from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.order_by("id")
    form = TodoForm()

    context = {"todo_list": todo_list, "form": form}

    return render(request, "index.html", context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=form.data["text"])
        new_todo.save()

    return redirect("index")


def complete_todo(request, todo_id):
    todo: Todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect("index")


def delete_completed(request):
    completed_todos = Todo.objects.filter(completed=True)
    completed_todos.delete()

    return redirect("index")
