from django.db import models
from django.db.models import CharField
from django_mysql.models import ListCharField

# Create your models here.

class PageData(models.Model):
    language = models.CharField(max_length=25, primary_key = True)
    emotions = ListCharField(base_field=CharField(max_length=25), size = 10, max_length = (25 * 10))
    public_faces = ListCharField(base_field=CharField(max_length=25), size = 10, max_length = (25 * 10))