from django.db import models
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    def __str__(self):
        return self.title
class Register(models.Model):
    email=models.EmailField(max_length=20)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.username