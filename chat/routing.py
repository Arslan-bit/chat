# routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"^ws/$", consumers.UserConsumer.as_asgi()),
]





# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r"^ws/$", consumers.MyConsumer.as_asgi()),
#     # re_path(r"^ws/$", consumers.UserConsumer.as_asgi()),
                                                     
# ]






























# chat/routing.py
# from django.urls import re_path

# from . import consumers

# websocket_urlpatterns = [
#     re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
# ]


