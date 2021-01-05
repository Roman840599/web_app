from channels.generic.websocket import AsyncWebsocketConsumer


class AsyncChatJsonConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        print(self.scope)
        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    'message': text_data,
                }
        )

    # async def receive(self, te):
    #     # message = content['message']
    #     # print(reciever)
    #     # await self.send_json(content=content)
    #     # await self.channel_layer.group_send(
    #     #     self.group_name,
    #     #     {
    #     #         'type': 'chat.message',
    #     #         'message': message,
    #     #     }
    #     # )

    async  def chat_message(self, event):
        await self.send(event['message'])

