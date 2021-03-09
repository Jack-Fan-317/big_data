from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
# Create your views here.
from .models import City


def cityData(request):
    city_all = City.objects.all()
    list_city = []
    for i in city_all:
        dict = {"name": i.city_name, "value": i.data}
        list_city.append(dict)
    # print(list_city)
    return JsonResponse({"data":{"data":list_city}})