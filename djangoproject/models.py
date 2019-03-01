from django.db import models

class tableValues(models.Model):
    name       = models.CharField(max_length=100)
    value      = models.IntegerField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)