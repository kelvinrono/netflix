
from django.conf.urls import url,include
from django.contrib import admin
from django_registration.backends.one_step.views import RegistrationView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('netflixapp.urls')),
    url('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/', include('django_registration.backends.one_step.urls')),

   

]
