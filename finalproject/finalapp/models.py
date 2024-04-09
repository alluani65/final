from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Genere(models.Model):
    genere=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    image=models.ImageField(upload_to='genere')
    class Meta:
        ordering=['genere',]
        verbose_name='Genere'
        verbose_name_plural='Generes'
    def get_url(self):
        return reverse('finalapp:genere',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.genere)

class Movie(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    poster=models.ImageField(upload_to='media')
    desc=models.TextField()
    date=models.DateField()
    actors=models.CharField(max_length=250)
    genere=models.ForeignKey(Genere,on_delete=models.CASCADE)
    link=models.URLField()
    added_by=models.ForeignKey(User,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)
    def get_url(self):
        return reverse('finalapp:genere_detail',args=[self.genere.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.title)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    def __str__(self):
     return f"Review for {self.movie.title} by {self.user.username}"
