from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from StudentApi.models import StudentInfo
from StudentApi.serializers import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def studentInfo(request,id=None):
    if request.method == 'GET' and id: 
        studentById= StudentInfo.objects.filter( StudentRollNo = id ) 
        student_serialize = StudentSerializer(studentById,many=True)
        return JsonResponse(student_serialize.data,safe = False)
        
    elif request.method == 'GET':
        students = StudentInfo.objects.all().order_by('StudentRollNo')
        student_serialize = StudentSerializer(students,many=True)
        return JsonResponse(student_serialize.data,safe=False)

    if request.method == 'POST':
        requestBody = JSONParser().parse(request)
        serializeBody = StudentSerializer(data=requestBody)
        if serializeBody.is_valid():
            serializeBody.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed Check data",safe = False)
    
    if request.method == 'DELETE':
        student = StudentInfo.objects.get(StudentRollNo=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)
