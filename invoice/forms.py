from django.forms import ModelForm
from .models import Invoice

class InvoiceCreateForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceEditForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'