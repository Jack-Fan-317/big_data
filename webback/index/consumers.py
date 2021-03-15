from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import City

class ChatConsumer(WebsocketConsumer):
    # 信息连接时
    def connect(self):
        self.accept()

    # 断开连接时
    def disconnect(self, close_code):
        pass

    # 信息接收时
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        # message = text_data_json['message']

        message = chat_code_to_msg(text_data_json['msg'])

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

def chat_code_to_msg(msg):
    city_all_1 = City.objects.all()
    list_city_1 = []
    for i in city_all_1:
        list_c = [i.city_name, i.data]
        list_city_1.append(list_c)
        list_c = []
    res = {
        "data":{
            "header": ["城市","数量"],
            "data":list_city_1,
            "index": True,
            "columnWidth": [50],
            "align": ['center'],
            "carousel": 'page'
        }
    }
    return res
    
                