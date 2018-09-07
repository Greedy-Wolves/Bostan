from django.db import models

# Create your models here.


class Department(models.Model):
    id = models.DecimalField(max_digits=2, decimal_places=0, primary_key=True)
    name = models.CharField(max_length=50)
