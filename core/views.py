from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import Movie

from core.forms import MovieForm

def homepage(request):
  return render(request, 'core/homepage.html')

def upload(request):
  if request.method == 'POST' and request.FILES['photo']:
    photo = request.FILES['photo']
    fss = FileSystemStorage()
    file = fss.save(photo.name, photo)
    file_url = fss.url(file)
    return render(request, 'core/upload.html', {'file_url': file_url})
  return render(request, 'core/upload.html')

def upload_modelform(request):
  if request.method == 'POST':
    form = MovieForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    return redirect("core:upload-modelform")
  form = MovieForm()
  movies = Movie.objects.all()
  return render(request=request, template_name='core/upload-modelform.html', context={'form': form, 'movies': movies}) 