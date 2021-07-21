
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home,ProfileList,ProfileCreate,Watch,ShowMovie, ShowMovieDetail


urlpatterns=[
 url(r'^mymovies', views.movies, name='myMovies'),
 url(r'^movie/(\d+)', views.single_movie, name = 'oneMovie'),
 url(r'^singlemovies/',views.single_movie, name = 'singles'),
url('',Home.as_view()),
url('profile/',ProfileList.as_view(),name='profile_list'),
url('profile/create/',ProfileCreate.as_view(),name='profile_create'),
url('watch/<str:profile_id>/',Watch.as_view(),name='watch')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


