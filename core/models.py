from django.db import models

class Movie(models.Model):
  file = models.FileField(upload_to='documents/')
  image = models.ImageField(upload_to='images/')