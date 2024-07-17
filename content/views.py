from django.shortcuts import render
from .models import Project

def projects_view(request):
  projects = Project.objects.all()
  return render(request, 'content/projects_list.html', {
    'projects_list': projects,
  })