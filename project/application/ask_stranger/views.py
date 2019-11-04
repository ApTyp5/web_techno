from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request, page = 1):
    return HttpResponse("index")
def hot(request, page = 1):
    return HttpResponse("hot")
def tagged(request, tag = 'def', page = 1):
    return HttpResponse("tagged")
def question(request, qu_id='def'):
    return HttpResponse("question")
def login(request):
    return HttpResponse("login")
def signup(request):
    return HttpResponse("signup")
def ask(request):
    return HttpResponse("ask")
