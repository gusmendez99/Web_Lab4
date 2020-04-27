from django.db import models

# Create your models here.
class Parent(models.Model):
    username = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name