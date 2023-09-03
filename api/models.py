from django.db import models
import string
import random

def generate_unique_code():
    length = 4 

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) #will generate code k length (4) containing uppercase ASCII chars
        if Room.objects.filter(code=code).count() == 0: #filter all room objects by codes and check if code is equal to generated code
            break #break if none of the objects meet criteria of code=code

    return code

# Create your models here.

class Room(models.Model):
    #Class attributes for each room
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True) #unique code for every room
    host = models.CharField(max_length=50, unique=True) #one host per room aka unique
    guest_can_pause = models.BooleanField(null=False, default=False) #must pass a value in
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True) #will automatically add date/time room was created
    current_song = models.CharField(max_length=50, null=True)

