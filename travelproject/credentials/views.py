from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request,"login.html")



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassw = request.POST['password1']

        if password==cpassw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=f_name,last_name=l_name,email=email)
                user.save();
                return redirect('login')


        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def logout(requset):
    auth.logout(requset)
    return redirect('/')
