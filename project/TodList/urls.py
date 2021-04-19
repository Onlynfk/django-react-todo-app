from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('teams/', views.teams, name="teams"),
    path('board/', views.todo_board, name="todo_board"),
    path('settings/', views.user_settings, name="user_settings"),
    path('profile/', views.user_profile, name="user_profile"),

    
]