from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def first(request):
    return HttpResponse('my project 3 sucess guys')


def second(request):
    return HttpResponse('my project 4 sucess guys')
