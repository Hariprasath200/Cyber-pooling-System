# models.py
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
