from django.shortcuts import render

def registration(request):
    return render(request, 'pages/registration.html')


def login(request):
    return render(request, 'pages/login.html')
# Create your views here.
