from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
   
import googlemaps
import time



def paginaInicial(request):





    key = "AIzaSyBv6UieBEcwH2nK91GpQ-BpzPnQBybco6E"



    gmaps = googlemaps.Client(key= key)

    places_result = gmaps.places_nearby(location = "-8.189868, -34.954734", radius = 5000, open_now = False, type = "restaurant")

    print(places_result)
        
    
    return JsonResponse(places_result)
