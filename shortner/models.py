from django.db import models

# Create your models here.
class URLShortner(models.Model):
    link = models.TextField(max_length=100000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return self.uuid
