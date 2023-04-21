from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Invoice
from .forms import InvoiceCreateForm, InvoiceEditForm

class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = 'invoice_create.html'
    success_url = '/invoice'

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice_detail.html'

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice.html'

class InvoiceEditView(UpdateView):
    model = Invoice
    form_class = InvoiceEditForm
    template_name = 'invoice_edit.html'
    success_url = '/'

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoice_delete.html'
