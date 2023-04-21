from django.forms import ModelForm
from .models import Customer

class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerEditForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'