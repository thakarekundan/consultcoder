from django.contrib import admin
from voucher.models import voucher_data,merchant
# Register your models here.

class Voucher(admin.ModelAdmin):
    fields = [
        'code',
        'amount',
        'startTime',
        'endTime',
        'redeemed'
    ]
    list_display = ('code','amount','startTime','endTime','redeemed')


admin.site.register(voucher_data, Voucher)

# class Merchant(admin.ModelAdmin):
#     fields = [
#         'code',
#         'amount',
#         'startTime',
#         'endTime',
#         'mobile',
#         'merchant_redeem'
#     ]
#     list_display = ('code','amount','startTime','endTime','mobile','merchant_redeem')

# admin.site.register(merchant)
