from django.db import models

# Create your models here.
class Link(models.Model):
    def __str__(self):
        return self.Name

    address = models.CharField(max_length=1000, null=True, blank=True)
    Name = models.CharField(max_length=1000, null=True, blank=True)