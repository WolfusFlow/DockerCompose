from django.db import models

class valueTable(models.Model):
    value = models.IntegerField()
    # name = models.CharField(max_length=60)
    created_time = models.DateTimeField(auto_now_add=True)
