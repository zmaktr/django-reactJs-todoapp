from django.db import models

class React(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=600)
