from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def save(request,name,rollno,age,marks,address):
	st=Student(name=name,rollno=rollno,age=age,marks=marks,address=address)
	st.save()
	return HttpResponse("Post Query")


def get_all(request):
	st=Student.objects.all()
	student=[i.name for i in st]
	response=".".join(student)
	return HttpResponse(response)

def get_data(request,name):
	st=Student.objects.get(name=name)
	return HttpResponse(st.name)

def delete(request,name):
	st=Student.objects.get(name=name).delete()
	return HttpResponse("Delete successfully done")

def max_mark(request):
	st=Student.objects.all()
	student=[i.name for i in st if i.marks>=70]
	response=".".join(student)
	return HttpResponse(response)
