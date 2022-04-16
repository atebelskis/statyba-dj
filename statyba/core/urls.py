from django.contrib import admin
from django.urls import path
from .views import CustomerListView, main_page, CustomerCreateView

#User: Alfa
#psw: Alfa1234

urlpatterns = [
        path('', main_page, name='home'),
        path('customer/', CustomerListView.as_view(), name='customer'),
        path('customer_create/', CustomerCreateView.as_view(), name='customer_create'),

]
