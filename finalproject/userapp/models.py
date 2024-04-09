from django.db import models
from finalapp.views import Movie,Genere
from django.contrib.auth.models import User
# Create your models here.

class FavouriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username}'s Favorite: {self.movie.title}"