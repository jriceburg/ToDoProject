from django.db import models


# Create your models here.

class TodoListDB(models.Model):
    task_item_db = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.task_item_db
