from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

# Create your models here.


class Upload(models.Model):

    #validator to set the maximum size of a file to 4gb
    def validate_file(fieldfile_obj):
        file_size = fieldfile_obj.file.size
        gigabyte_limit = 4.0
        if file_size > gigabyte_limit * 1024 * 1024 * 1024:
            raise ValidationError("Max file size is %sGB" % str(gigabyte_limit))

    name = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True, validators=[validate_file])

    #if you want to go the detail view use this instead
    # def get_absolute_url(self):
    #     return reverse('upload:detail', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('upload:success')

    def __str__(self):
        return self.name
