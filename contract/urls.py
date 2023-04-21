
from django.urls import path
from .views import *

urlpatterns = [
    path('', ContractListView.as_view(), name='main_contract'),
    path('contract-create/', ContractCreateView.as_view(), name='contract_create'),
    path('contract-detail/<pk>', ContractDetailView.as_view(), name='contract_detail'),
    # path('contract-detail/<pk>', contract_detail_view, name='contract_detail'),
    path('contract-edit/<pk>', ContractEditView.as_view(), name='contract_edit'),
    path('contract-delete/<pk>', ContractDeleteView.as_view(), name='contract_delete'),
    ]