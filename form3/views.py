from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .forms import *

# def main_form3(request):
#     return render(request, 'form3.html')

class Form3ListView(ListView):
    model = Form3
    template_name = 'form3.html'

class Form3CreateView(CreateView):
    model = Form3
    form_class = Form3CreateForm
    template_name = 'form3_create.html'
    success_url = '/'

class Form3DetailView(DetailView):
    model = Form3
    template_name = 'form3_detail.html'

class Form3EditView(UpdateView):
    model = Form3
    form_class = Form3EditForm
    template_name = 'form3_edit.html'
    success_url = '/'

class Form3DeleteView(DeleteView):
    model = Form3
    template_name = 'form3_delete.html'