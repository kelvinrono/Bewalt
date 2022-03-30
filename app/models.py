from django.db import models

# Create your models here.

class Client(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField(max_length=255)
    message=models.TextField(max_length=1000)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.name