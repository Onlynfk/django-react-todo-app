from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'todList/index.html')

def dashboard(request):
    return render(request, 'todList/dashboard.html')


def todo_board(request):
    return render(request, 'todList/todo_board.html')

def user_settings(request):
    return render(request, 'todList/user_settings.html')

def user_profile(request):
    return render(request, 'todList/user_profile.html')