from django.urls import path
from . import views 

app_name = 'core'

urlpatterns = [
  path('', views.homepage, name='homepage'),
  path('upload', views.upload, name='upload'),
  path('upload-modelform', views.upload_modelform, name='upload-modelform'),
]