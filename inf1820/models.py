from django.db import models

# Create your models here.

class Question( models.Model ):    
    question    = models.TextField( null = True );
    answer      = models.TextField( null = True );
    score       = models.IntegerField( default = 1 );
    
class Tag( models.Model ):
    name        = models.CharField( max_length = 80 );
    targets     = models.ManyToManyField( Question );