from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectListView.as_view(), name='main_project'),
    path('project-create/', ProjectCreateView.as_view(), name='project_create'),
    path('project-detail/<pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project-edit/<pk>', ProjectEditView.as_view(), name='project_edit'),
    path('project-delete/<pk>', ProjectDeleteView.as_view(), name='project_delete')
    ]