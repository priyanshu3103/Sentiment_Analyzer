from django.db import models
from django.db import models

class AnalyzedText(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=20)

