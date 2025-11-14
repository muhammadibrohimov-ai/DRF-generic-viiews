from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=50)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname
    

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    desc = models.TextField()
    year = models.PositiveIntegerField(validators=([MinValueValidator(1)]))
    price = models.PositiveIntegerField(validators=([MinValueValidator(1)]))
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name