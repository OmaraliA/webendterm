from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(default = timezone.now)
   
def _str_(self):
    return self.title
