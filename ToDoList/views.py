from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from .forms import TodoListForm
from .models import TodoListDB


# Create your views here.
# retrieve all the records from the DB and render them
def todo_index(request):
    # query the DB and store in one variable and pass the variable to the
    # render function via the context method
    form = TodoListForm()
    todo = TodoListDB.objects.all()
    context = {'todo_DB': todo, 'form': form}
    return render(request, 'TodoList/todo_index.html', context)


def todo_add(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST or None)
        if form.is_valid():
            list_items = form.save(commit=False)
            list_items.completed = False
            list_items.created_at = datetime.now()
            # server side validation before information is saved to the DB
            list_items.save()
            # if the form is valid then save to DB then redirect the user to the page that lists the products
        return redirect('todo_index')
    else:
        form = TodoListForm()
        context = {'form_add': form}
    return render(request, 'TodoList/todo_index.html', context)


def todo_update(request, id):
    todo = TodoListDB.objects.get(id=id)
    form = TodoListForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_index')
    context = {'todo_DB': todo, 'form': form}
    return render(request, 'TodoList/todo_update.html', context)


def todo_delete(request, id):
    todo = TodoListDB.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_index')
    else:
        context = {'todo': todo}
        return render(request, 'TodoList/todo_delete.html', context)


def todo_complete(request, id):
    todo = TodoListDB.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect('todo_index')