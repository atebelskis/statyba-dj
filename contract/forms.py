from django.forms import ModelForm
from .models import Contracts

class CreateContractForm(ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'

class EditContractForm(ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'

class ContractViewForm(ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'
