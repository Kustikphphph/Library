from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>Глaвнaя</h2>")
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")

