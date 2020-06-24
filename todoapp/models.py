from django.db import models
from django.contrib.auth import get_user_model


class Todo(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    objects = models.Manager

    def __str__(self):
        return self.title