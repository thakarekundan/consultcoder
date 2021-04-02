from django.shortcuts import render
from voucher.forms import Add_Voucher,Dist_Voucher,Merchant_Dist_Voucher,registration
from django.http import HttpResponse
from voucher.models import voucher_data,merchant,contact,Consumer_contact
import random
import datetime
from django.utils import timezone
x = timezone.now()
# Create your views here.


def home(request):
	return render(request,"voucher/home.html")

def add_voucher(request):
	if request.method == 'POST':
		form = Add_Voucher(request.POST)
		if form.is_valid():
			total_number=form.cleaned_data['Total_number']
			amount=form.cleaned_data['Amount']
			st=form.cleaned_data['startTime']
			et=form.cleaned_data['endTime']
			for i in range(0,total_number):
				r_code=random.randint(1000,9999)
				voucher_data(code=r_code,amount=amount,startTime=st,endTime=et).save()
			return render(request,"voucher/add_voucher.html")

	form=Add_Voucher()
	return render(request,"voucher/add_voucher.html",{'form':form})

def get_voucher(request):
	data = voucher_data.objects.all()
	d = {"code":[],"amount":[],"st":[],"et":[],"redeem":[]};
	for i in data:
		if i.startTime<=x and i.endTime>=x:
			d["code"].append(i.code)
			d["amount"].append(i.amount)
			d["st"].append(i.startTime)
			d["et"].append(i.endTime)
			d["redeem"].append(i.redeemed)
    
	books= zip(d["code"], d["amount"], d["st"], d["et"],d["redeem"])
	return render(request,"voucher/get_voucher.html",{'context':books})


def dist_voucher(request):
	if request.method == 'POST':
		form = Dist_Voucher(request.POST)
		if form.is_valid():
			code=form.cleaned_data['code']
			mobile=form.cleaned_data['mobile']
			b=voucher_data.objects.get(code=code)
			b.redeemed=True
			b.save()
			merchant.objects.get_or_create(voucher=voucher_data(code=code))
			contact.objects.get_or_create(voucher_id=voucher_data(code=code),mobile=mobile)
			return render(request,"voucher/home.html")

	form=Dist_Voucher()
	return render(request,"voucher/distribute_voucher.html",{'form':form})


def merchant_dashboard(request):
	return render(request,"voucher/merchant_dashboard.html")

def merchant_get_voucher(request):
	data = merchant.objects.all().values()
	print(data)
	l_code=[]
	m_red=[]
	val=0
	for i in data:
		l_code.append(data[val]['voucher_id'])
		m_red.append(data[val]['merchant_redeemed'])
		val+=1
	print(l_code)
	print(m_red)
	d = {"code":[],"amount":[],"st":[],"et":[],"redeem":m_red};
	for i in l_code:
		k=voucher_data.objects.get(code=i)
		if k.startTime<=x and k.endTime>=x:
			d["code"].append(k.code)
			d["amount"].append(k.amount)
			d["st"].append(k.startTime)
			d["et"].append(k.endTime)
	
	# d["redeem"].append(m_red)
	print(d)
	details= zip(d["code"], d["amount"], d["st"], d["et"],d["redeem"])
	return render(request,"voucher/merchant_get_voucher.html",{'context':details})

def merchant_distribute(request):
	if request.method == 'POST':
		form = Dist_Voucher(request.POST)
		if form.is_valid():
			code=form.cleaned_data['code']
			mobile=form.cleaned_data['mobile']
			b=merchant.objects.get(voucher=voucher_data(code=code))
			b.merchant_redeemed=True
			b.save()
			Consumer_contact.objects.get_or_create(cid=voucher_data(code=code),mobile=mobile)
			return render(request,"voucher/merchant_dashboard.html")

	form=Dist_Voucher()
	return render(request,"voucher/merchant_distribute.html",{'form':form})




def reg(request):
	if request.method == 'POST':
		form =registration(request.POST)
		if form.is_valid():
			mobile=form.cleaned_data['mobile_no']
			if Consumer_contact.objects.filter(mobile=mobile).count()==0:
				return HttpResponse("Not valid mobile number")
			else:
				data=Consumer_contact.objects.filter(mobile=mobile).values()
				l_code=[]
				val=0
				for i in data:
					l_code.append(data[val]['cid_id'])
					val+=1
				print(l_code)
				d = {"code":[],"amount":[],"st":[],"et":[]};
				for i in l_code:
					k=voucher_data.objects.get(code=i)
					if k.startTime<=x and k.endTime>=x:
						d["code"].append(k.code)
						d["amount"].append(k.amount)
						d["st"].append(k.startTime)
						d["et"].append(k.endTime)
				details= zip(d["code"], d["amount"], d["st"], d["et"])
				return render(request,"voucher/consumer_get.html",{'context':details})


	form=registration()
	return render(request,"voucher/registration.html",{'form':form})
 












# def get_all(request):
# 	st=Student.objects.all()
# 	student=[i.name for i in st]
# 	response=".".join(student)
# 	return HttpResponse(response)

# def get_data(request,name):
# 	st=Student.objects.get(name=name)
# 	return HttpResponse(st.name)

# def delete(request,name):
# 	st=Student.objects.get(name=name).delete()
# 	return HttpResponse("Delete successfully done")

# def max_mark(request):
# 	st=Student.objects.all()
# 	student=[i.name for i in st if i.marks>=70]
# 	response=".".join(student)
# 	return HttpResponse(response)
