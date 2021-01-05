from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='in/login')
def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='in/login')
def about(request):
    return render(request, 'main/about.html')