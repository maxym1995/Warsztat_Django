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
        if name != "" and capacity != "":
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

#display list of all rooms
def all_rooms(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        if len(rooms) == 0:
            return HttpResponse("No rooms avaliable")
        else:
            return render(request, "all_rooms.html", context={"rooms": rooms})

#display room details
def room_details(request,room_id):
    if request.method == "GET":
        room = Room.objects.get(id=room_id)
        r_name = room.name
        r_capacity = room.capacity
        r_proj = room.projector_aval
        return render(request, "room_details.html", context={"r_name": r_name, "r_capacity":r_capacity, "r_proj":r_proj})

def room_modify(request,room_id):
    pass

def room_delete(request,room_id):
    pass

def room_reserve(request,room_id):
    pass