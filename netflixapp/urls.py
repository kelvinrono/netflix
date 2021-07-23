
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from django.urls import path
from django.contrib.auth import views as auth_views
=======
from django.urls import path, include 
>>>>>>> 021a44c960b7732c65c18f9f8f41553872f0c4fa
from .views import Home,ProfileList,ProfileCreate,Watch,ShowMovie, ShowMovieDetail


urlpatterns=[
 url(r'^mymovies', views.movies, name='myMovies'),
 url(r'^movie/(\d+)', views.single_movie, name = 'oneMovie'),
<<<<<<< HEAD
 url(r'^singlemovies/',views.single_movie, name = 'singles'),
 url(r'login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
 url(r'signup/', auth_views.LoginView.as_view(template_name='accounts/signup.html'), name='signup'),
 url('',Home.as_view()),
 url('profile/',ProfileList.as_view(),name='profile_list'),
 url('profile/create/',ProfileCreate.as_view(),name='profile_create'),
 url('watch/<str:profile_id>/',Watch.as_view(),name='watch')
=======
url('',Home.as_view()),
url('profile/',ProfileList.as_view(),name='profile_list'),
url('profile/create/',ProfileCreate.as_view(),name='profile_create'),
url('watch/<str:profile_id>/',Watch.as_view(),name='watch'),
path('account/', include('django.contrib.auth.urls')),


>>>>>>> 021a44c960b7732c65c18f9f8f41553872f0c4fa
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


