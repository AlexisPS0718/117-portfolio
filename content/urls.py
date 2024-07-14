from django.urls import path
from content import views

urlpatterns = [
  path('', views.projects_view, name='projects'),
]