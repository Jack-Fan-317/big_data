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


from channels.generic.websocket import WebsocketConsumer
import json
import time

# Create your views here.
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        """
        接收消息
        :param text_data: 客户端发送的消息
        :return:
        """
        print(text_data)
        poetryList = [
            "云想衣裳花想容",
            "春风拂槛露华浓",
            "若非群玉山头见",
            "会向瑶台月下逢",
        ]
        for i in poetryList:
            time.sleep(0.5)
            self.send(i)