from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.models import FavouriteMovie
from django.core.paginator import Paginator, EmptyPage
# Create your views here.


# @login_required
# def add_favourite(request, movie_id):
#     favourite_movie, created = FavouriteMovie.objects.get_or_create(user=request.user,movie_id=movie_id)
#     if created:
#         pass
#     return redirect('userapp:favourite')

@login_required
def add_favourite(request, movie_id):
    favourite_movie, created = FavouriteMovie.objects.get_or_create(user=request.user, movie_id=movie_id)
    if created:
        pass
    favourite_movies = FavouriteMovie.objects.filter(user=request.user)
    paginator = Paginator(favourite_movies, 6)  
    
    page_number = request.GET.get('page', 1)
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    return render(request, 'favourite.html', {'favourite': page})

@login_required
def list_favourite(request):
    favourite_movies = FavouriteMovie.objects.filter(user=request.user)
    return render(request, 'favourite.html', {'favourite': favourite_movies})

@login_required
def remove_favourite(request, movie_id):
    favour=FavouriteMovie.objects.filter(user=request.user, movie_id=movie_id)
    favour.delete()
    return redirect('userapp:favourite')