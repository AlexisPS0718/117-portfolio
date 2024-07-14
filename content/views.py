from django.shortcuts import render

def projects_view(request):
  return render(request, 'content/projects_list.html')