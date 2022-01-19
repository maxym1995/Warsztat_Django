from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
import random
from room_booking_app.models import *

# this is to check if template was loaded correctly on server
def server(request):
    return render(request, "server.html")