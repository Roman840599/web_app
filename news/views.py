from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/in/login')
def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


@login_required(login_url='in/login')
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Incorrect validation'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)