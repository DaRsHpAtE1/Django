from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StudentModel
from .ser import StudentSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def stuop(request):
    if request.method == 'POST':
        record = StudentSerializer(data=request.data)
        if record.is_valid():
            record.save()
            return Response({'msg': 'Record Inserted'})
        else:
            return Response(record.errors)
    elif request.method == 'GET':
        result = StudentModel.objects.all()
        sresult = StudentSerializer(result, many=True)
        return Response(sresult.data)
