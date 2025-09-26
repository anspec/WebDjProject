from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> Это мой первый проект на джанго </h1>")

def new(request):
    return HttpResponse("<h1> Это вторая страница моего первого проекта на джанго </h1>")

def data(request):
    return HttpResponse("<h1> Это страница 'data' моего первого проекта на джанго </h1>")

def test(request):
    return HttpResponse("<h1> Это страница 'test' моего первого проекта на джанго </h1>")
