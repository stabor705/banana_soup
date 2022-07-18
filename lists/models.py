from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=50)
    repeats = models.BooleanField()
    user = models.ForeignKey(get_user_model(), models.CASCADE)

    def __str__(self):
        return self.name
    
class Entry(models.Model):
    text = models.CharField(max_length=255)
    lst = models.ForeignKey(List, models.CASCADE, db_column="list", related_name="entries")
    done = models.BooleanField()

    def __str__(self):
        return self.text[:50]
