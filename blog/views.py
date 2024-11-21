from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Главная</h2>")

# def user(request):
#     age = request.GET.get("age")
#     name = request.GET.get("name")
#     return HttpResponse(F"<h2>Name: {name} Age: {age}</h2>")

def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(F"<h2>Name: {name} Age: {age}</h2>")