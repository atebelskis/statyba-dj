from django.forms import ModelForm
from .models import Customer

class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerDetailForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerEditForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'bank_code', 'invoice_number', 'phone', 'email']
        #fields = '__all__'

