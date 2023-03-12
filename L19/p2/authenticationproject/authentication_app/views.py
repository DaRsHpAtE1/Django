from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import *

# Create your views here.
mm = [
    'Never Gonna Give You Up',
    'Never Gonna Let You Down',
    'Never Gonna Run Around and Desert You',
    'Never Gonna Make You Cry',
    'Never Gonna Say Goodbye',
    'Never Gonna Tell a Lie and Hurt You',
    'OOOOOOOOOOOO',
    'Never Gonna Give.. Never Gonna Give..',
    'Give You Up',
    'Never Gonna Let.. Never Gonna Let..',
    'Let You Down',
]


@api_view(['GET'])
def msg(request):
    r = randint(0, len(mm)-1)
    message = mm[r]
    return Response({'message': message})
