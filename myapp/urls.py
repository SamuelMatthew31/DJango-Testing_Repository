from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
    path("about/", views.about, name="about"),
    path('todos/<int:pk>/toggle/', views.todo_toggle, name='todo_toggle'),  # ← baris baru
]
