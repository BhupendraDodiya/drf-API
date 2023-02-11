from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

#Model Object - Single Student Data

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializers(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# Query set - all student data

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
