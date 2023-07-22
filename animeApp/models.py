from django.db import models

# Create your models here.

class AnimeApp(models.Model):
    
    # Attributes of the class
    name = models.CharField(max_length=50, blank=False, default='')
    author = models.CharField(max_length=50, blank=False, default='')
    rating = models.DecimalField(decimal_places=2, max_digits=3, blank=False, default=0.0)
    releaseDate = models.CharField(max_length=50, blank=False, default='')
    
    def __str__(self):
        return self.name    
    
    # Inner class to sort the records according to their id
    class Meta:
        ordering = ('id', )