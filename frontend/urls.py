from django.urls import path
from .views import index

urlpatterns = [
    path('', index), #render index template wherever there is blank path
    path('info', index),
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index)
]
