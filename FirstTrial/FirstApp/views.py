from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("I am from index() function")

def PrintPage(request):
    return render(request, "PrintPage.html")