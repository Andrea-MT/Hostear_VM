from django.http import JsonResponse
from django.shortcuts import render

alumnos = [
    {"nombre": "Andrea Mendoza", "matricula": "18001354"},
    {"nombre": "Carlos May", "matricula": "18001347"},
    {"nombre": "Mishel Mendoza", "matricula": "18001455"},
    {"nombre": "Max Mendoza", "matricula": "21206789"},
    {"nombre": "Mario Alberto", "matricula": "17009087"}
]

profesores = [
    {"nombre": "María Álvarez", "numeroEmpleado": "EMP001"},
    {"nombre": "Hades Lorenzo", "numeroEmpleado": "EMP002"},
    {"nombre": "Quira Cen", "numeroEmpleado": "EMP003"},
    {"nombre": "Lorenzo Mendoza", "numeroEmpleado": "EMP004"},
    {"nombre": "Marisol Mendoza", "numeroEmpleado": "EMP005"}
]

def get_alumnos(request):
    return JsonResponse({"alumnos": alumnos})

def get_profesores(request):
    return JsonResponse({"profesores": profesores})

def index(request):
    return render(request, 'index.html')