from django.db import models

class Plan(models.Model):
    Item = models.CharField(max_length=500)
