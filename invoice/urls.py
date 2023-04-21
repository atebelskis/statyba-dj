from django.urls import path
from .views import *

urlpatterns = [
    path('', InvoiceListView.as_view(), name='main_invoice'),
    path('invoice-create', InvoiceCreateView.as_view(), name='invoice_create'),
    path('invoice-detail/<pk>', InvoiceDetailView.as_view(), name='invoice_detail'),
    path('invoice-edit/<pk>', InvoiceEditView.as_view(), name='invoice_edit'),
    path('invoice-delete/<pk>', InvoiceDeleteView.as_view(), name='invoice_delete'),
]