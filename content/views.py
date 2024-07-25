from django.shortcuts import render
from .models import Project

def projects_view(request):
  projects = Project.objects.all()
  return render(request, 'pages/index.html', {
    'projects_list': projects,
  })