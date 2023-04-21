from django.urls import path
from .views import *

urlpatterns = [
    path('', CustomerListView.as_view(), name='main_customer'),
    path('customer-create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer-detail/<pk>', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer-edit/<pk>', CustomerEditView.as_view(), name='customer_edit'),
    path('customer-delete/<pk>', CustomerDeleteView.as_view(), name='customer_delete'),
    ]