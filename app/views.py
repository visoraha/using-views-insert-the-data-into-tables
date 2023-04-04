from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_data(reuqest):
    CI=input('enter cid')
    CN=input('enter course name')
    TN=input('enter trainer name')
    COU=Course.objects.get_or_create(cid=CI,cname=CN,tname=TN)[0]
    COU.save()
    
    return HttpResponse('data is inserted')
def student_data(request):
    SI=input('enter student id :')
    SN=input('enter student name :')
    CI=Course.objects.get_or_create(cid=101)[0]
    STD=Student.objects.get_or_create(sid=SI,sname=SN,cid=CI)[0]
    STD.save()

    return HttpResponse('data is inserted')
def exam(request):
    SI=Student.objects.get_or_create(sid=2)[0]
    MA=input('enter marks')
    EX=Exam.objects.get_or_create(sid=SI,marks=MA)[0]
    EX.save()
    return HttpResponse('data is inserted')
