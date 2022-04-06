
from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "id",
            "flightNumber",
            "operatingAirlines",
            "departureCity",
            "arrivalCity",
            "dateOfDeparture",
            "estimatedTimeOfDeparture",
        )


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = (
            "id",
            "firstName",
            "lastName",
            "email",
            "phoneNumber",
        )


class ReservationSerializer(serializers.ModelSerializer):
#Bir rezervatıon içinde birden cok kullanıcı olacagı için many=True
#Reservationdan passengere gecerken ismi passenger belirlediğimiziçin passenger yazdık
    passenger = PassengerSerializer(many=True, required=False)
#flight dtabasede flight_id olarak kayıt edilir
    flight = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all())
    # flight_id = serializers.IntegerField()
#user databasede user_id olarak kayıt  edilir 
#StringRelatedField() metodu ile strsinde ne yazmıssam onu user e atadık Buda sadece readonly bir fielddir
#stringRelatedField() olarak tanımladığımızı create için kulanamayız.Ama user_id yi gönderebiliriz
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",
            "passenger",
            "user",
            "user_id",
        )

    def create(self, validated_data):
        print(validated_data)
        passenger_data = validated_data.pop('passenger')
        print(passenger_data)
        validated_data["user_id"] = self.context['request'].user.id
        reservation = Reservation.objects.create(**validated_data)
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)
        reservation.save()

        return reservation


class StaffFlightSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = (
            "flightNumber",
            "operatingAirlines",
            "departureCity",
            "arrivalCity",
            "dateOfDeparture",
            "estimatedTimeOfDeparture",
            "reservations",
        )
