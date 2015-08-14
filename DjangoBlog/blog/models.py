from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SHORT_TEXT = 1000

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):    # __str__ en python3
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT:
            return self.text[:SHORT_TEXT]
        else:
            return self.text
