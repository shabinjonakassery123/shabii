from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout


from .models import reg, registration, empreg, empreg1, admintest, custpost


def display(request):
    return render(request,'first.html')


def reg1(request):
    if (request.method == 'POST'):
        a = request.POST['n1']
        b = int(request.POST['n2'])
        c = request.POST['n3']
        d = request.POST['n4']
        e = request.POST['n5']
        f = request.POST['n6']
        data = reg.objects.create(Username=a,Password=b)
        data.save()
        data1 = registration.objects.create(name=c,age=d,address=e,phone=f)
        data1.save()
        return HttpResponse('<script>{ alert("REGISTRATION COMPLETE") } </script>')

def profile1(request):
    if 'id' in request.session:
        return render(request, 'custprofile.html')
    else:
        return redirect(log1)


def log1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = int(request.POST['n2'])
        data = reg.objects.get(Username=a)
        if (data.Password == b):
            request.session['id'] = a
            return redirect(profile1)
        else:
            return HttpResponse('<script>{ alert("LOGIN FAILED") } </script>')
    else:
        return render (request,'custlogin.html')

def logout1(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(log1)

def regemp1(request):
    if (request.method == 'POST'):
        a = request.POST['n1']
        b = int(request.POST['n2'])
        c = request.POST['n3']
        d = request.POST['n4']
        e = request.POST['n5']
        f = request.POST['n6']
        g = request.POST['n7']
        data = empreg.objects.create(username=a,password=b)
        data.save()
        data1 = empreg1.objects.create(name=c,age=d,qualification=e,job=f,phone=g)
        data1.save()
        return HttpResponse('<script>{ alert("REGISTRATION COMPLETED") } </script>')

def second1(request):
    return render(request,'empreg.html')

def register1(request):
    return render(request,'custreg.html')

def pro1(request):
    return render(request,'uprofile.html')

def custupdate(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        registration.objects.filter(name=a).update(age=b,address=c,phone=d)
    return HttpResponse('<script>{ alert("UPDATED SUCCESSFULLY ") } </script>')

def main11(request):
    data = empreg1.objects.all()
    return render(request, 'custprofile.html', {'sh': data})


def search1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        f = registration.objects.filter(name=a)
    return render(request,'uprofile.html',{'s':f})

def contact1(request):
    return render (request,'contact.html')

def message1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        s = custpost.objects.create(text=a)
        s.save()
    return HttpResponse('<script>{ alert("SENT") } </script>')


                           #ADMINVIEWS


def admpr1(request):
    if 'id' in request.session:
        return render(request,'admintemp.html')
    else:
        return redirect(admlog1)


def admlog1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = int(request.POST['n2'])
        c = admintest.objects.get(username=a)
        if(c.password==b):
            request.session['id'] = a
            return redirect(admpr1)
        else:
            return HttpResponse('<script>{ alert("LOGIN FAILED ") } </script>')
    else:
        return render(request,'adminlog.html')

def logoutemp1(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(admlog1)


def adminemp1(request):
    a = empreg1.objects.all()
    return render(request,'employee.html',{'s':a})


def adup1(request):
    if request.method=='POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        e = request.POST['n5']
        empreg1.objects.filter(name=a).update(age=b,qualification=c,job=d,phone=e)
        return HttpResponse('<script>{ alert("UPDATED") } </script>')

def ademp1(request):
    return render(request,'empreg.html')

def adupg1(request):
    return render(request,'adsearch.html')

def adsr1(request):
    if request.method=='POST':
        a = request.POST['n1']
        b = empreg1.objects.filter(name=a)
        return render(request,'adsearch.html',{'as':b})

def adlt1(request):
    return render(request,'adelt.html')

def adele1(request):
    if request.method==('POST'):
        a = request.POST['n1']
        b = empreg1.objects.filter(name=a)
        return render(request,'adelt.html',{'as':b})

def adte1(request):
    if request.method=='POST':
        a = request.POST['n1']
        data = empreg1.objects.filter(name=a)
        data.delete()
        return HttpResponse('<script>{ alert("DELETED") } </script>')

def adcst1(request):
    data = registration.objects.all()
    return render(request,'adcust.html',{'s':data})

def adcup1(request):
    return render(request,'cup.html')

def adcu1(request):
    if request.method=='POST':
        a = request.POST['n1']
        b = registration.objects.filter(name=a)
        return render(request,'cup.html',{'as':b})

def adcup21(request):
    if request.method=='POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        registration.objects.filter(name=a).update(age=b,address=c,phone=d)
        return HttpResponse('<script>{ alert("UPDATED") } </script>')

def adcud1(request):
    return render(request,'custreg.html')

def adcudele1(request):
    return render(request,'custdelete.html')

def acde1(request):
    if request.method==('POST'):
        a = request.POST['n1']
        b = registration.objects.filter(name=a)
        return render(request,'custdelete.html',{'as':b})

def adcdle1(request):
    if request.method=='POST':
        a = request.POST['n1']
        data = registration.objects.filter(name=a)
        data.delete()
        return HttpResponse('<script>{ alert("DELETED") } </script>')


def adpr1(request):
    s = admintest.objects.all()
    return render(request,'adprofileup.html',{'a':s})

def adprup1(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        admintest.objects.filter(name=a).update(password=b)
        return HttpResponse('<script>{ alert("UPDATED") } </script>')

def ee1(request):
    s = custpost.objects.all()
    return render(request,'custadmpost.html',{'a':s})


