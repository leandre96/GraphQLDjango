from django.db import models

# Create your models here.
class Animal(models.Model):
    name=models.CharField(max_length=20)
    genus=models.CharField(max_length=20)
    is_domesticated=models.BooleanField()

    def __str__(self):
        return self.name
