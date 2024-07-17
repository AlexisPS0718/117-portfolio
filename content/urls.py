from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from content import views

urlpatterns = [
  path('', views.projects_view, name='projects'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)