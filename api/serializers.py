from rest_framework import serializers
from .models import Profile,Board,NewTask,Task

# Serializers define the API representation.
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')
       

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('__all__')
   

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')
   



