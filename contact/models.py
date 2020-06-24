from django.db import models

class Contact(models.Model):
    name = models.CharField(blank=True, max_length=200)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    objects = models.Manager

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.email