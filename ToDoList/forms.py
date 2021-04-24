from django import forms
from .models import TodoListDB


# use a class to create forms, this will inherit from the forms class
class TodoListForm(forms.ModelForm):
    # use Meta class to connect model directly to
    class Meta:
        model = TodoListDB
        fields = '__all__'

        widgets = {
            'task_item_db': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


