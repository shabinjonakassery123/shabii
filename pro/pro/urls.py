"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display),
    path('reg',views.reg1),
    path('log',views.log1),
    path('logout',views.logout1),
    path('first',views.profile1),
    path('regemp',views.regemp1),
    path('second',views.second1),
    path('register',views.register1),
    path('profile',views.pro1),
    path('search',views.search1),
    path('update',views.custupdate),
    path('main1',views.main11),
    path('contact',views.contact1),
    path('message',views.message1),

              #ADMIN URL

    path('admlog',views.admlog1),
    path('third',views.admpr1),
    path('aa',views.adminemp1),
    path('adup',views.adup1),
    path('ademp',views.ademp1),
    path('adupg',views.adupg1),
    path('adsr',views.adsr1),
    path('adlt',views.adlt1),
    path('adele',views.adele1),
    path('adte',views.adte1),
    path('bb',views.adcst1),
    path('adcup',views.adcup1),
    path('adcu',views.adcu1),
    path('adcup2',views.adcup21),
    path('adcud',views.adcud1),
    path('adcudele',views.adcudele1),
    path('acde',views.acde1),
    path('adcdle',views.adcdle1),
    path('dd',views.adpr1),
    path('adprup',views.adprup1),
    path('ee',views.ee1),
    path('logoutemp',views.logoutemp1)




]
