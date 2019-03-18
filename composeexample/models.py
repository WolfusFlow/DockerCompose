from django.db import models

class valueTable(models.Model):
    text = models.CharField(max_length=100) #"Your Value: "
    value = models.IntegerField()
    #TextInfo = models.CharField(max_length=100)