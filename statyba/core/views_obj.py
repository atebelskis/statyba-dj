from django.views.generic import ListView
from .models import ConstProject

class ProjectListView(ListView):
    model = ConstProject
    template_name = 'project_list.html'
    success_url = '/'

