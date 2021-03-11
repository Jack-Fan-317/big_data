from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

# class ChatConsumer(WebsocketConsumer):
#     # 信息连接时
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accept()

#     # 断开连接时
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     # 信息接收时
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))





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
        # message = chat_code_to_msg(text_data_json['code'],text_data_json['msg'])

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': 'websocket!'
        }))
        
    # def chat_code_to_msg(code,msg):
    #     if code == 100:
    #         token = msg