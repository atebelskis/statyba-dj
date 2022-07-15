# from django.shortcuts import render
# from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
#
# from django.http import HttpResponse, request
# from django.shortcuts import render
# from .forms import CustomerCreateForm, CustomerEditForm #CustomerDetailForm
#
#
# def main_page(request):
#     return render(request, 'home.html')
#
#
# class CustomerListView(ListView):
#     model = Customer
#     template_name = 'customer/customer.html'
#     success_url = '/'
#     context_object_name = 'customer'
#
#
#
#
# class CustomerCreateView(CreateView):
#     model = Customer
#     form_class = CustomerCreateForm
#     template_name = 'customer/customer_create.html'
#     success_url = '/'
#
# class CustomerDetailView(DetailView):
#     model = Customer
#     fields = '__all__'
#     #form_class = CustomerDetailForm
#     template_name = 'customer/customer_detail.html'
#     success_url = '/customer/'
#     #context_object_name = 'customer'
#
#
#
#     def get_context_data(self, **kwargs):   #naudojame , kad .....??????
#         context = super().get_context_data(**kwargs)
#         #context['customer'] = Customer.objects.all()
#         return context
#
#
#
# class CustomerEditView(UpdateView):
#     model = Customer
#     form_class = CustomerEditForm
#     template_name = 'customer/customer_edit.html'
#     success_url = '/customer/'
#
# class CustomerDeleteView(DeleteView):
#     model = Customer
#     template_name = 'customer/customer_delete.html'
#     success_url = '/customer/'
#
