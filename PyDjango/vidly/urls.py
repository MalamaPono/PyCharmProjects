"""vidly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api.models import MovieResource
from . import views

movie_resource = MovieResource()

# when certain url patterns are triggered, django will chop off that portion of the url and pass the rest
# of the url to be processed in the next module which will keep passing it on and passing it on and navigating
# to new pages until the entire url is finished processing.
urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path("movies/",include("movies.urls")),
    path('api/',include(movie_resource.urls))
]
