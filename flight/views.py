
from .models import Flight, Reservation
from .serializers import FlightSerializer
from rest_framework import viewsets
from .permissions import IsStuffOrReadOnly

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
#tuple kullandığımız için sonunna virgül koyduk
    permission_classes =  (IsStuffOrReadOnly,)