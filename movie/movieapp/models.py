from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
