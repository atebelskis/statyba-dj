from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from .forms import *
from .models import Contracts

# def main_contract(request):
#     return render(request, 'contract.html')

class ContractCreateView(CreateView):
    model = Contracts
    form_class = CreateContractForm
    template_name = 'contract_create.html'
    success_url = '/'

class ContractEditView(UpdateView):
    model = Contracts
    form_class = EditContractForm
    template_name = 'contract_edit.html'
    success_url = '/contract/'

class ContractListView(ListView):
    model = Contracts
    template_name = 'contract.html'
    success_url = '/'

class ContractDetailView(DetailView):
    model = Contracts
    form_class = ContractViewForm
    template_name = 'contract_detail.html'
    success_url = '/'
    
    # def get_context_data(self, **kwargs):
    #     context = super(ContractDetailView, self).get_context_data()
    #     context['sutartis'] = Contracts.objects.all()
    #     return context

class ContractDeleteView(DeleteView):
    model = Contracts
    template_name = 'contract_delete.html'
    success_url = '/contract/'

# def contract_detail_view(request):
#     context = {'contract_number': Contracts.number}
#     return render(request, 'contract+detail.html', context)