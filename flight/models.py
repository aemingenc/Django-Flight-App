from django.db import models
from django.contrib.auth.models import User
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=25)
    departureCity = models.CharField(max_length=30)
    arrivalCity = models.CharField(max_length=30)
#bunu kullanıcı girecek bu yüzden auto_now koymadık
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return f'{self.flightNumber} -{self.departureCity} -{self.arrivalCity}'




class Passenger(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    updateDate = models.DateTimeField(auto_now=True)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#bir rezervasyonda birden fazla yolcusu olabilir bir yolcununda birden fazla rezervasyonu olabilir
#Bu yuzden manyto many ile bagladık.related n
#passenger modelinden rezervation modeline ulasmak için rezervation_set diye ulasabilirdik kolayolsun diye
#related_name belirledik
    passenger = models.ManyToManyField(Passenger, related_name='passenger')
#Hangi flightnin rezervasyonu olduğunu göstercek bu yüzden bagladık
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name='reservations')