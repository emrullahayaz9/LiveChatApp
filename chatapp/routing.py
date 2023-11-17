from django.urls import path
from . import consumers

websocket_urlpattern = [

    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi())
]

# whenever using asgi, we have to make some config in the asgi.py file
# we have to say that we use urlpattern for async routing