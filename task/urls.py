from django.urls import path

from . import views


urlpatterns = [
    path('task/', views.TaskListCreateAPIView.as_view()),
    path('task/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view()),
]
