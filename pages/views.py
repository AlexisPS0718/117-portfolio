from django.shortcuts import render, redirect
from django.core.mail import send_mail
from content.models import Project
from .forms import contact_form

def index_view(request):
  projects = Project.objects.all()
  
  if request.method == "POST":
    form = contact_form(request.POST)

    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']

      send_mail(subject, message + "\n\n" + name, email, ['alxpesa@gmail.com'])

      return redirect('index')
    else:
      print("Invalid form")
  else:
    form = contact_form()

  return render(request, 'pages/index.html', {
    'form': form,
    'projects_list': projects,
  })