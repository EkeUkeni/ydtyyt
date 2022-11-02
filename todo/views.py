from django.shortcuts import render, redirect
# from django.http import HttpResponse
import datetime
from todo.models import TodoList
from todo.forms import TodoForm
# Create your views here.


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

# def current_datetime(request):
#     now = datetime.datetime.now()
#     # html = "<html><body>It is now %s.</body></html>" % now
#     context = {
#         "current_time":now,
#         "name": "BRAIN",
#     }
#     return render(request, "index_old.html", context)


def get_todos(request):
    """
    filter method only returns what we want to see
    """
    todo_lists = TodoList.objects.all().order_by("-created_at", "title")
    # todo_lists = TodoList.objects.filter(complete=True)
    # print(todo_lists)
    context =  {
        "todo_lists": todo_lists
    }
    return render(request, "index.html", context)

def get_todo(request, pk):

    todo = TodoList.objects.get(pk=pk)
    print(todo)
    context = {
        "todo":todo
    }
    return render(request, "todo.html", context)

def create_todo(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()

        return redirect('todo-list')

    context = {
        "form":form,
        "title":"create",
    }
    return render(request, "create_update_todo.html", context)


def update_todo(request, pk):
    todo = TodoList.objects.get(pk=pk)
    form = TodoForm(instance=todo)

    if request.method == "POST":
        form = TodoForm(request.POST or None, instance=todo)
        if form.is_valid():
            form.save()

        return redirect('todo-list')

    context = {
        "form":form,
        "title":"update",
    }
    return render(request, "create_Update_todo.html", context)

def delete_todo(request, pk):
    todo = TodoList.objects.get(pk=pk)

    if request.method == "POST":
        todo.delete()
        return redirect("todo-list")


    # todo.delete()

    # return redirect("todo-list")

    context = {
        "todo":todo
    }

    return render(request, "confirm_delete.html", context)
