from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    bio = models.TextField()
    joind_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# holds the cardboxes and cards created by the user
class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NewTask(models.Model):
    title = models.CharField(max_length=25) 
    
    def __str__(self):
        return self.title
  
class Task(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_task = models.ForeignKey(NewTask, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    body = models.TextField(blank=True,null=True)
    duartion = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name