from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Upload(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True)
    downloaded = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('upload:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Folder(models.Model):
    Upload = models.ForeignKey(Upload, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=255)