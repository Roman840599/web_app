from django.shortcuts import render, redirect
from django.views.generic.edit import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm


def RegisterUser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration.html', context)


class Login(View):
    form = LoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                if auth_user.is_active:
                    login(request, auth_user)
                    return render(request, 'main/index.html')
            else:
                template_name = 'invalid_login.html'
                return render(request, template_name)
        return render(request, self.template_name, {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')