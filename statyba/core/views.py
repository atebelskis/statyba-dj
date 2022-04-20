from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Customer
from django.http import HttpResponse, request
from django.shortcuts import render
from .forms import CustomerCreateForm, CustomerDetailForm, CustomerEditForm


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

class CustomerDetailView(DetailView):
    model = Customer
    form_class = CustomerDetailForm
    template_name = 'customer_detail.html'
    success_url = '/customer/'


class CustomerEditView(UpdateView):
    model = Customer
    form_class = CustomerEditForm
    template_name = 'customer_edit.html'
    success_url = '/customer/'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = '/customer/'
