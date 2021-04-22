from django.db import models
from django.contrib.auth.models import User

# holds the cardboxes and cards created by the user
class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True,null=True)
    # image = models.ImageField(upload_to="")
    bio = models.TextField()


class Dashboard(models.Model):
    pass

# the card, is the tasks the user creates  
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True,blank=True)
    body = models.TextField(blank=True,null=True)
    duartion = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# the  box, that holds multiple cards
class CardBox(models.Model):
    title = models.CharField(max_length=25) # a title in the cardbox is always needed bfore adding cards in it
    

    def __str__(self):
        return self.title





    