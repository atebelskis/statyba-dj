from django.forms import ModelForm
from .models import ConstrProject

class ProjectCreateForm(ModelForm):
    class Meta:
        model = ConstrProject
        fields = '__all__'

class ProjectEditForm(ModelForm):
    class Meta:
        model = ConstrProject
        fields = '__all__'

