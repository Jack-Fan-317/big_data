from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
# Create your views here.
from .models import City


def cityData1(request):
    city_all_1 = City.objects.all()
    list_city_1 = []
    for i in city_all_1:
        list_c = [i.city_name, i.data]
        list_city_1.append(list_c)
        list_c = []
    print(list_city_1)
    return JsonResponse(
        {
            "data":{
                "header": ["城市","数量"],
                "data":list_city_1,
                "index": True,
                "columnWidth": [50],
                "align": ['center'],
                "carousel": 'page'
            }
        }
    )


def cityData2(request):
    city_all_2 = City.objects.all()
    list_city_2 = []
    for i in city_all_2:
        dict = {"name": i.city_name, "value": i.data}
        list_city_2.append(dict)
    print(list_city_2)
    return JsonResponse(
        {
            "data":{
                "data":list_city_2
            }
        }
    )