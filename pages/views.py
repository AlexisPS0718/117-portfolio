from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import contact_form

def about_view(request):
  return render(request, 'pages/home.html')

def contact_view(request):
  if request.method == "POST":
    form = contact_form(request.POST)

    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']

      send_mail(subject, message + "\n\n" + name, email, ['alxpesa@gmail.com'])

      return redirect('home')
    else:
      print("Invalid form")
  else:
    form = contact_form()

  return render(request, 'pages/contact.html', {
    'form': form,
  })