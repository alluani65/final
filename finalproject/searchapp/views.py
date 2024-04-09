from django.shortcuts import render
from finalapp.models import Movie,Genere
from django.db.models import Q
# Create your views here.

# def movie_search(request):
#     query = request.GET.get('q')
#     genere_id = request.GET.get('genere')
#     movies = Movie.objects.all()

#     if query:
#         movies = movies.filter(Q(title__icontains=query) | Q(desc__icontains=query))

#     if genere_id:
#         movies = movies.filter(genere_id=genere_id)

#     genere = Genere.objects.all()

#     return render(request, 'search.html', {'movie': movies, 'genere': genere})

def movie_search(request):
    movie=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movie=Movie.objects.all().filter(Q(title__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'query':query,'movie':movie})