from django.db import models
from django.utils import timezone

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    introduce = models.TextField()
    pub_date = models.DateTimeField('date published', default = timezone.now)

    def __str__(self):
        return self.name

    
        

    
