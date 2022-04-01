from django.db import models

# Create your models here.

class Client(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField(max_length=1000)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    image=models.ImageField()
    description=models.CharField(max_length=255)
    title=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="galleries"

    def __str__(self):
        return self.title