from django.db import models

# Create your models here.
class File(models.Model):
    filename = models.CharField(max_length=100)
    size = models.IntegerField(max_length=50000)
    status = models.CharField(max_length=100)
    datetime_file = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='media')
    url = models.CharField(max_length=100)


    def __str__(self):
        return self.filename



