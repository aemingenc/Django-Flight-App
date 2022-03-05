from django.urls import path
from rest_framework import routers
from .views import FlightView

#bir router objesi belirledik
router = routers.DefaultRouter()
#register metodu ile ilk önce flights/sonra flightWiewden gelen yazzın dedik
router.register('flights', FlightView)

urlpatterns = [

]

#routerı url patternse ekledik
urlpatterns += router.urls