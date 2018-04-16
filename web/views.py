from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(requests):
    return render(requests, 'web/index.html')


def home(requests):
    string = u"学习django"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(requests, 'web/home.html', {'string': string,'TutorialList':TutorialList})


def hello(requests):
    return HttpResponse("Hello world!")


def add(requests):
    A = requests.GET.get('a', 0)
    B = requests.GET.get('b', 0)
    C = int(A)+int(B)
    return HttpResponse(str(C))


def add2(requests, a, b):
    return HttpResponse(str(int(a)+int(b)))
