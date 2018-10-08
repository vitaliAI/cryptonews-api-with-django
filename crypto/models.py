from django.db import models
from django.urls import reverse

# Create your models here.

class CryptoNews(models.Model):
    title = models.CharField(max_length=300, unique=True)
    imageurl = models.URLField(max_length=300)
    body = models.TextField()
    source = models.CharField(max_length=50)
    source_url = models.URLField(max_length=300)
    source_id = models.CharField(max_length=20)
    sentiment = models.FloatField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.source_id])
