from django.http.response import HttpResponse
from django.shortcuts import redirect, render

def home(request):
    return render(request, 'base.html')