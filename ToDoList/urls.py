from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_index, name="todo_index"),
    path('add', views.todo_add, name="todo_add"),
    path('update/<str:id>', views.todo_update, name="todo_update"),
    path('delete/<str:id>', views.todo_delete, name="todo_delete"),
    path('complete/<str:id>', views.todo_complete, name="todo_complete"),
]
