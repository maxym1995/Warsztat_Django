from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
import random
from room_booking_app.models import *

# this is to check if template was loaded correctly on server
def server(request):
    return render(request, "server.html")
#base template
def base(request):
    return render(request, "base_template.html")

# add new room
def new_room(request):
    if request.method == "GET":
        return render(request,"new_room_template.html")
    if request.method == "POST":
        name = request.POST.get("room-name")
        capacity = request.POST.get("capacity")
        if request.POST.get("projector") == "on":
            projector = True
        else:
            projector = False
        rooms = Room.objects.all()
        rooms_names = []
        error_message=""
        for r in rooms:
            rooms_names.append(r.name)
        if name is not "" and capacity is not "":
            if name in rooms_names:
                error_message = "This name has been already used."
                return render(request, "new_room_template.html", context={"error_message": error_message})
            else:
                if int(capacity) > 0 and int(capacity) <=100:
                    Room.objects.create(name=name, capacity=capacity, projector_aval = projector)
                    return HttpResponseRedirect("/base")
                else:
                    error_message = "Capacity has to be number between 1 to 100."
                    return render(request, "new_room_template.html", context={"error_message": error_message})
        else:
            error_message = "Name and capacity have to be filled in."
            return render(request, "new_room_template.html", context={"error_message": error_message})
