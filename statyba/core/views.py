from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Customer
from django.http import HttpResponse, request
from django.shortcuts import render
from .forms import CustomerCreateForm


def main_page(request):
    return render(request, 'home.html')


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer.html'
    success_url = '/'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'customer_create.html'
    success_url = '/'
