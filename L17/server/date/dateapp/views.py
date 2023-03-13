from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import *
# Create your views here.


@api_view(['GET'])
def dt(request):
    dt = datetime.now().date()
    msg = f'Server date is: {dt}'
    return Response({'msg': msg})


@api_view(['GET'])
def ti(request):
    ti = datetime.now().time()
    msg = f'Server time is: {ti}'
    return Response({'msg': msg})


@api_view(['GET'])
def dtti(request):
    dtti = datetime.now()
    msg = f'Server date and time is: {dtti}'
    return Response({'msg':msg})