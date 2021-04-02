"""kundan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views 
from voucher import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save/<str:name>/<int:rollno>/<int:age>/<int:marks>/<str:address>',views.save),
    path('get_all',views.get_all),
    path('get_data/<str:name>',views.get_data),
    path('delete/<str:name>',views.delete),
    path('max_mark',views.max_mark),


    path('',v.home),
    path('add_voucher/',v.add_voucher),
    path('get_voucher/',v.get_voucher),
    path('distribute_voucher/',v.dist_voucher),

    path('merchant_dashboard/',v.merchant_dashboard),
    path('merchant_get_voucher/',v.merchant_get_voucher),
    path('merchant_distribute/',v.merchant_distribute),

    path('registration/',v.reg),
    ]