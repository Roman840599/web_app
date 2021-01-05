from django.conf.urls import url
from .consumers import AsyncChatJsonConsumer


websocket_urls = [
    # url(r'^ws/chat/$', AsyncChatJsonConsumer.as_asgi()),
    url(r'^ws/chat/(?P<group_name>\w+)/$', AsyncChatJsonConsumer.as_asgi()),
]