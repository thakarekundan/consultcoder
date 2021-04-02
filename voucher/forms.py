from django import forms

class Add_Voucher(forms.Form):
	Total_number=forms.IntegerField(label="Total Number of voucher to generate")
	Amount = forms.FloatField(label="Amount")
	startTime = forms.DateTimeField(label="Start Time")
	endTime = forms.DateTimeField(label="End Time")

class Dist_Voucher(forms.Form):
	code = forms.CharField(label="Enter voucher code")
	mobile = forms.CharField(label="Enter Consumers mobile number")

class Merchant_Dist_Voucher(forms.Form):
	code = forms.CharField(label="Enter voucher code")
	mobile = forms.CharField(label="Enter Consumers mobile number")

class registration(forms.Form):
	mobile_no = forms.CharField(label="Enter Mobile Number")