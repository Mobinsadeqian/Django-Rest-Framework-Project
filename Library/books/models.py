from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
