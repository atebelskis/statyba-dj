from django.urls import path
from .views import *

urlpatterns = [
    path('', Form3ListView.as_view(), name='main_form3'),
    path('form3-create', Form3CreateView.as_view(), name='form3_create'),
    path('form3-detail/<pk>', Form3DetailView.as_view(), name='form3_detail'),
    path('form3-edit/<pk>', Form3EditView.as_view(), name='form3_edit'),
    path('form3-delete/<pk>', Form3DeleteView.as_view(), name='form3_delete'),
]