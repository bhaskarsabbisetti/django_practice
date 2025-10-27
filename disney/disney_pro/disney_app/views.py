from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Coders

# Create your views here.
@csrf_exempt
def marvel(req):
    print(req.method)
    return HttpResponse("marvel movie is playing")

details=[{
    "id_":1,
    "name":"anvesh",
    "profession":"CEO",
    "gender":"male"
},
{
    "id_":2,
    "name":"bharath",
    "profession":"astronat",
    "gender":"female"
}
]
def users_data(req,id):
    for i in details:
        if id==i["id_"]:
            return JsonResponse({"responce":i})
    return JsonResponse({"msg":"user does not exist"})
@csrf_exempt
def dc(req):
    if req.method=="GET":
        return HttpResponse("welcome to this page")
    else:
        return HttpResponse("Invalid method")
@csrf_exempt
def register(req):
    
    # details.append(json.loads(req.body))
    d=json.loads(req.body)
    for i in details:
        if i["id_"]==d["id_"]:
            print(i["id_"],d["id_"])
            return JsonResponse({"msg":"user already exist"})
        else:
            details.append(d)
    return JsonResponse({"msg":"register successful"})
@csrf_exempt
def registeration(req):
    user_name=req.POST.get("name")
    user_age=req.POST.get("age")
    coder=Coders.objects.create(name=user_name,age=user_age)
    coder.save
    return HttpResponse("successfully posted")

