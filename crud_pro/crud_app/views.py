from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Faculty
from django.shortcuts import render
import json
from .serializers import FacultySerializer
# Create your views here.
def greetings(req):
    return HttpResponse("hello faculty good to see you")

@csrf_exempt
def faculty_data(req,id=None):
    if req.method=='GET':
        if id:
            fac_data=Faculty.objects.filter(id=id).values().first()
            return JsonResponse({"faculty":fac_data})
        total_faculty=Faculty.objects.all().values()
        return JsonResponse({"faculty":list(total_faculty)})
    
def template(req):
    return render(req,'myapp/form.html')

@csrf_exempt
def register(req):
    if req.method=='POST':
        fac_data=json.loads(req.body)
        id_=fac_data['id']
        if Faculty.objects.filter(id=id_).exists():
            return JsonResponse({'msg':"faculty already exist"})
        else:
            fac=Faculty.objects.create(id=fac_data['id'],f_name=fac_data['f_name'],l_name=fac_data['l_name'],mail=fac_data["mail"],branch=fac_data["branch"])
            return JsonResponse({"msg":"registerd successfully"})
        

@csrf_exempt
def update_faculty(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            fac = Faculty.objects.get(id=id)
            fac.f_name = data.get('f_name', fac.f_name)
            fac.l_name = data.get('l_name', fac.l_name)
            fac.mail = data.get('mail', fac.mail)
            fac.branch = data.get('branch', fac.branch)
            fac.save()
            return JsonResponse({"message": "Faculty updated successfully"})
        except Faculty.DoesNotExist:
            return JsonResponse({"error": "Faculty not found"}, status=404)

@csrf_exempt
def fac_update(request, id):
    if request.method == 'PATCH':
        try:
            fac = Faculty.objects.get(id=id)
            data = json.loads(request.body)

            if 'f_name' in data:
                fac.f_name = data['f_name']
            if 'l_name' in data:
                fac.l_name = data['l_name']
            if 'mail' in data:
                fac.mail = data['mail']
            if 'branch' in data:
                fac.branch = data['branch']

            fac.save()
            return JsonResponse({
                "message": "Faculty updated successfully",
                "faculty": {
                    "id": fac.id,
                    "f_name": fac.f_name,
                    "l_name": fac.l_name,
                    "mail": fac.mail,
                    "branch": fac.branch
                }
            })

        except Faculty.DoesNotExist:
            return JsonResponse({"error": "Faculty not found"}, status=404)

@csrf_exempt
def delete_faculty(request, id):
    if request.method == 'DELETE':
        try:
            fac = Faculty.objects.get(id=id)
            fac.delete() 
            return JsonResponse({"message": "Faculty deleted successfully"})
        except Faculty.DoesNotExist:
            return JsonResponse({"error": "Faculty not found"}, status=404)
@csrf_exempt
def faculty_form(req):
    if req.method=="POST":
        id=req.POST.get('id')
        f_name=req.POST.get('f_name')
        l_name=req.POST.get('l_name')
        branch=req.POST.get('branch')
        email=req.POST.get('email')
        Faculty.objects.create(id=id,f_name=f_name,l_name=l_name,mail=email,branch=branch)
        return render(req,'myapp/form.html',{'msg':'successfully registered'})
    return render(req,'myapp/form.html')

@csrf_exempt
def upd_faculty(req,id):
    try:
        single_fac=Faculty.objects.get(id=id)
        fac_data=json.loads(req.body)
        serializer=FacultySerializer(single_fac,data=fac_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("faculty updated")
    except:
        return HttpResponse('user not found')

    