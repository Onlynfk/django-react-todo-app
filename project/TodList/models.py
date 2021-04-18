from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True,null=True)
    # image = models.ImageField(upload_to="")
    bio = models.TextField()


class Dashboard(models.Model):
    pass