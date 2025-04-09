from django.urls import path

from . import views

urlpatterns = [
    path("alumnos", views.get_alumnos, name="get_alumnos"),
    path("profesores", views.get_profesores, name="get_profesores"),
    path("", views.index, name="index"),
]