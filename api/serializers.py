from rest_framework import serializers
from .models import Room

#Translate Room model from models.py into Json response - convert into strings
#Serialization is process of converting data object into series of bytes that saves state of object in easily transmittable form

class RoomSerializer(serializers.ModelSerializer): #take room object and return as response
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at', 'current_song') #automattically ID field in every model

class CreateRoomSerializer(serializers.ModelSerializer): #data being sent in post request is valid
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])

    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')