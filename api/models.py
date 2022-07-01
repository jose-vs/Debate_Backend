from django.db import models

class Topic(models.Model): 
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
