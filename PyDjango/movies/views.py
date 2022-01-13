from django.shortcuts import render
from django.http import HttpResponse, Http404
from.models import Movie
from django.shortcuts import render, get_object_or_404

# Create your views here.

# index represents the main page of an app
def index(request):
    movies = Movie.objects.all()
    return render(request,"movies/index.html",{"movies":movies})

def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request,'movies/detail.html',{'movie':movie})

# Movies.objects.all()
# # select all movies from movies_movie
#
# Movies.objects.filter(release_year=1984)
# # select From movies_movie where release year is 1984
#
# Movies.objects.get(id=1)
# # get the movie with an id of 1