from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import UserRegisterForm
from .models import User
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate


def main_page(request):
    return render(request, 'index.html')


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = '/login'

def user_login(request):
    if request.method == "POST":
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')