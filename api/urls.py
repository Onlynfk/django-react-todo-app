from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverViewAPI),

    path('profile/', views.ProfileView.as_view()),
    path('profile-create/', views.ProfileCreate.as_view()),
    path('profile-retrieve/<int:pk>/', views.ProfileRetrieve.as_view()),
    path('profile-update/<int:pk>/', views.ProfileUpdate.as_view()),
    path('profile-delele/<int:pk>/', views.ProfileDelete.as_view()),


    path('task/', views.TaskView.as_view()),
    path('task-create/', views.TaskCreate.as_view()),
    path('task-retrieve/<int:pk>/', views.TaskRetrieve.as_view()),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view()),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view()),

    path('board/', views.BoardView.as_view()),
    path('board-create/', views.BoardCreate.as_view()),
    path('board-retrieve/<int:pk>/', views.BoardRetrieve.as_view()),
    path('board-update/<int:pk>/', views.BoardUpdate.as_view()),
    path('board-delete/<int:pk>/', views.BoardDelete.as_view()),

]