from django.shortcuts import render
from .models import Customer
from .forms import CustomerEditForm, CustomerCreateForm
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'customer_create.html'
    success_url = '/'

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerEditView(UpdateView):
    model = Customer
    template_name = 'customer_edit.html'
    form_class = CustomerEditForm
    success_url = '/'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'


