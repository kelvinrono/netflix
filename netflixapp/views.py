from django.shortcuts import render
from datetime import datetime, date
import time
import json
from time import mktime
import tmdbsimple as tmdb
from googleapiclient.discovery import build
from django.shortcuts import render,redirect
from django.views import View
from .models import Movie, Profile
from .forms import ProfileForm
#from .forms import NetflixForm


# Create your views here.
#API KEYS and Request Parameters
tmdb.API_KEY = '7da36f8f0eb36fe41793378a726e9104'
DEVELOPER_KEY = 'AIzaSyCZKLBjdBQA7RIFL9uwy8z2BpDWeA0-p-s'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v4'

def movies(request):
    popular_movies = tmdb.Movies('popular')
    popular_movies = popular_movies.info()['results']

    upcoming_movies_tmdb = tmdb.Movies('upcoming')
    upcoming_movies = upcoming_movies_tmdb.info()['results']

    return render(request, 'movies.html', {'popular':popular_movies, 'upcoming':upcoming_movies})


def single_movie(request, id):
    popular_movies = tmdb.Movies('popular')
    popular_movies = popular_movies.info()['results']

    tittle=''

    for pop in popular_movies:
        if str(pop['id'])==str(id):
            tittle = pop['title']

    youtube = build('youtube','v3',developerKey = 'AIzaSyAzKbAFcUX8Gnclb_gauk6EV-VqAgDuX7w')
    req = youtube.search().list(q= tittle+'trailer',part = 'snippet',type= 'video').execute()

    return render(request, 'singles.html', {'reqs': req})






class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles=request.user.profiles.all()

        return render(request,'profileList.html',{'profiles':profiles})

class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form=ProfileForm()

        return render(request,'profileCreate.html',{
            'form':form
        })

    def post(self, request, *args, **kwargs):
        form=ProfileForm(request.POST or None)

        if form.is_valid():
            profile=Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect(f'/watch/{profile.uuid}')

        return render(request,'profileCreate.html',{'form':form})

class Watch(View):
    def get(self, request,profile_id, *args, **kwargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)

            movies=Movie.objects.filter(age_limit=profile.age_limit)

            try:
                showcase=movies[0]
            except :
                showcase=None
            

            if profile not in request.user.profiles.all():
                return redirect(to='core:profile_list')
            return render(request,'movieList.html',{
            'movies':movies,
            'show_case':showcase
            })
        except Profile.DoesNotExist:
            return redirect(to='core:profile_list')

class ShowMovieDetail(View):
    def get(self,request,movie_id,*args, **kwargs):
            try:
                
                movie=Movie.objects.get(uuid=movie_id)

                return render(request,'movieDetail.html',{
                    'movie':movie
                })
            except Movie.DoesNotExist:
                return redirect('core:profile_list')

class ShowMovie(View):
     def get(self,request,movie_id,*args, **kwargs):
            try:
                
                movie=Movie.objects.get(uuid=movie_id)

                movie=movie.videos.values()
                

                return render(request,'showMovie.html',{
                    'movie':list(movie)
                })
            except Movie.DoesNotExist:
                return redirect('core:profile_list')
