
from django.db import models

# Create your models here.

class Mental(models.Model):
    Year=models.IntegerField()
    Schizophrenia_disorders =models.FloatField(max_length=90)
    Depressive_disorders=models.FloatField(max_length=90)
    Anxiety_disorders=models.FloatField(max_length=90)
    Bipolar_disorders=models.FloatField(max_length=90)
    Eating_disorders=models.FloatField(max_length=90)