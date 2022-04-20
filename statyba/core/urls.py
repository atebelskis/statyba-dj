from django.contrib import admin
from django.urls import path
from .views import CustomerListView, main_page, CustomerCreateView, CustomerDetailView, CustomerEditView, CustomerDeleteView
from .views_obj import ProjectListView

#User: Alfa
#psw: Alfa1234

urlpatterns = [
        path('', main_page, name='home'),
        path('customer/', CustomerListView.as_view(), name='customer'),
        path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
        path('customer/detail/<pk>', CustomerDetailView.as_view(), name='customer_detail'),
        path('customer/edit/<pk>', CustomerEditView.as_view(), name='customer_edit'),
        path('customer/delete/<pk>', CustomerDeleteView.as_view(), name='customer_delete'),
        path('project/', ProjectListView.as_view(), name='project_list'),
]
