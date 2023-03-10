from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmployeeModel
from .sers import EmployeeSerializer
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def empop(request, i=None):
    if request.method == 'POST':
        record = EmployeeSerializer(data=request.data)
        if record.is_valid():
            record.save()
            return Response({'msg': 'Record Inserted'})
        else:
            return Response(record.errors)
    elif request.method == 'GET':
        result = EmployeeModel.objects.all()
        sresult = EmployeeSerializer(result, many=True)
        return Response(sresult.data)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        try:
            emp = EmployeeModel.objects.get(eid=i)
            emp.delete()
            return Response({'msg': 'Record Deleted'})
        except EmployeeModel.DoesNotExist:
            raise Http404
