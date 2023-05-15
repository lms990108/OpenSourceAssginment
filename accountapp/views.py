from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return render(request, 'accountapp/helloworld.html')


def post_list(request):
    return render(request, 'accountapp/post_list.html', {})
