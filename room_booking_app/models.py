from django.db import models

# Create your models here.
# from room_booking_app.models import *
class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    projector_aval = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)

#adding rooms (into shell):
# Room.objects.create(name='Mercury', capacity=4)
# Room.objects.create(name='Mars', capacity=4)
# Room.objects.create(name='Venus', capacity=6)
# Room.objects.create(name='Earth', capacity=8, projector_aval=True)
# Room.objects.create(name='Neptune', capacity=12,projector_aval=True)
# Room.objects.create(name='Uranus', capacity=15,projector_aval=True)
# Room.objects.create(name='Saturn', capacity=20,projector_aval=True)
# Room.objects.create(name='Jupiter', capacity=40,projector_aval=True)



class Reservation(models.Model):
    date = models.DateField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('room_id', 'date')
