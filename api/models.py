from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=50)
    note = models.TextField(verbose_name='note')
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name