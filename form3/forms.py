from django.forms import ModelForm
from .models import Form3

class Form3CreateForm(ModelForm):
    class Meta:
        model = Form3
        fields = '__all__'

class Form3EditForm(ModelForm):
    class Meta:
        models = Form3
        fields = '__all__'