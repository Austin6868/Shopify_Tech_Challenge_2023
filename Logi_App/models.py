from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=200, unique=True, default="default")
    city = models.CharField(max_length=200, default="default")
    state = models.CharField(max_length=200, default="default")
    size = models.CharField(max_length=200, null=True, default="0")
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name

class Inv_Item(models.Model):

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Logi_App')
    warehouse = models.ForeignKey(Warehouse, default="none", on_delete=models.SET_DEFAULT, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('Logi_App:single', args=[self.slug])

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
