from django.contrib import admin

# Register your models here.
from ToDoList.models import TodoListDB

admin.site.register(TodoListDB)
