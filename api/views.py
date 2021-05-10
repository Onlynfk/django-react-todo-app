from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
# Create your views here.


@api_view(['GET'])
def OverViewAPI(request):
    api_urls = {
        'OverViewAPI': 'http://127.0.0.1:8000/api/',

        'Board': 'http://127.0.0.1:8000/api/board/',
        'BoardCreate': 'http://127.0.0.1:8000/api/board/create/',
        'BoardRetrieve': 'http://127.0.0.1:8000/api/board-retrieve/<int:pk>/',
        'BoardDelete': 'http://127.0.0.1:8000/api/board-delete/<int:pk>/',

        'Task':'http://127.0.0.1:8000/api/profile/',
        'TaskCreate':'http://127.0.0.1:8000/api/profile-create/',
        'TaskRetrieve':'http://127.0.0.1:8000/api/profile-retrieve/<int:pk>/',
        'TaskUpdate':'http://127.0.0.1:8000/api/profile-update/<int:pk>/',
        'TaskDelete':'http://127.0.0.1:8000/api/profile-delete/<int:pk>/',

        'Profile':'http://127.0.0.1:8000/api/task/',
        'ProfileCreate':'http://127.0.0.1:8000/api/task-create/',
        'ProfileRetrieve':'http://127.0.0.1:8000/api/task-retrieve/<int:pk>/',
        'ProfileUpdate':'http://127.0.0.1:8000/api/task-update/<int:pk>/',
        'ProfileDelete':'http://127.0.0.1:8000/api/task-delete/<int:pk>/',
    }

    return Response(api_urls)


class BoardView(generics.ListAPIView):
    """
    Used for read-only endpoints to represent a collection of model instances.
    Provides a get method handler.
    """
    # restricted from public api
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all().order_by('-id') #latest board
    serializer_class = BoardSerializer

class BoardCreate(generics.CreateAPIView):
    """
    Used for create-only endpoints.
    Provides a post method handler.
    """
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardRetrieve(generics.RetrieveAPIView):
    """
    Used for read or update endpoints to represent a single model instance.
    Provides get, put and patch method handlers.
    """
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardUpdate(generics.RetrieveUpdateAPIView):
    """
    Used for read or update endpoints to represent a single model instance.
    Provides get, put and patch method handlers.
    """
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardDelete(generics.RetrieveDestroyAPIView):
    """
    Used for read or delete endpoints to represent a single model instance.
    Provides get and delete method handlers.
    """
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
class ProfileView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRetrieve(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ProfileDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TaskView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-id') #latest tasks
    serializer_class = TaskSerializer

class TaskCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieve(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


