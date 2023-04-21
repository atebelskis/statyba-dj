from django.shortcuts import render
from .models import ConstrProject
from .forms import ProjectCreateForm, ProjectEditForm
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

class ProjectCreateView(CreateView):
    model = ConstrProject
    form_class = ProjectCreateForm
    template_name = 'project_create.html'
    success_url = '/project'

class ProjectListView(ListView):
    model = ConstrProject
    template_name = 'project.html'

class ProjectDetailView(DetailView):
    model = ConstrProject
    template_name = 'project_detail.html'

class ProjectEditView(UpdateView):
    model = ConstrProject
    template_name = 'project_edit.html'
    form_class = ProjectEditForm
    success_url = '/project'

class ProjectDeleteView(DeleteView):
    model = ConstrProject
    template_name = 'project_delete.html'
    success_url = '/project'


