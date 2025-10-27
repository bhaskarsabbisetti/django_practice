from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Students
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def greetings(req):
    return HttpResponse("hello user good to see you!")
def student_data(req):
    if req.method=="GET":
        stu_data=Students.objects.all()
        dict_data=stu_data.values()
        list_data=list(dict_data)
        return JsonResponse({"all_data":list_data})
@csrf_exempt
def register(req):
    if req.method=="POST":
        stu_data=json.loads(req.body)
        id=stu_data["id"]
        f_name=stu_data["f_name"]
        l_name=stu_data["l_name"]
        branch=stu_data["branch"]
        new_stu=Students.objects.create(id=id,f_name=f_name,l_name=l_name,branch=branch)
        return HttpResponse(f"registerd succesfully {new_stu}")
@csrf_exempt
def stu_data(request, id):
    try:
        student = Students.objects.get(id=id)
        data = {
            "id": student.id,
            "f_name": student.f_name,
            "l_name": student.l_name,
        }
        return JsonResponse({"student": data})
    except Students.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)