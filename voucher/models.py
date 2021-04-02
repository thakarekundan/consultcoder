from django.db import models

# Create your models here.
class voucher_data(models.Model):
	code=models.CharField(max_length=10,primary_key=True)
	amount= models.FloatField()
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	redeemed = models.BooleanField(default=False)

class merchant(models.Model):
	voucher = models.OneToOneField(voucher_data,on_delete = models.CASCADE, related_name = 'addr_set')
	merchant_redeemed = models.BooleanField(default=False)

class contact(models.Model):
	voucher_id = models.OneToOneField(voucher_data,on_delete = models.CASCADE, related_name = 'code_set')
	mobile = models.CharField(max_length=10)

class Consumer_contact(models.Model):
	cid = models.OneToOneField(voucher_data,on_delete = models.CASCADE)
	mobile = models.CharField(max_length=10)