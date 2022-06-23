from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload(request):
  if request.method == 'POST' and request.FILES['upload']:
    upload = request.FILES['upload']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload)
    file_url = fss.url(file)
    return render(request, 'core/upload.html', {'file_url': file_url})
  return render(request, 'core/upload.html')