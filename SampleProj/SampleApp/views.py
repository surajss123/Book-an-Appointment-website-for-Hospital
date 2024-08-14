from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import appointment
from django.contrib.auth.decorators import login_required

# Create your views here.
login_required(login_url='signin')
def su1(request):
    return  render(request, "templates/index.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()

                # log user in and redirect to setting page

                user_login = auth.authenticate(username=username, password=password1)
                auth.login(request,user_login)

                # create a profile object for the new user

                user_model = User.objects.get(username=username)
                # new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                # new_profile.save()
                return redirect('index')

        else:
            messages.info(request,'Password not matching')
            return redirect('signup')

    return render(request,'signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('signin')
    return render(request,'signin.html')

login_required(login_url='signin')
def index1(request):
    return render(request,'index1.html')

login_required(login_url='signin')
def sur1(request):
    cd = appointment()
    cd.Name = request.POST.get("name")
    cd.Email = request.POST.get("email")
    cd.Phone = request.POST.get("phone")
    cd.Department = request.POST.get("department")
    cd.Doctor = request.POST.get("doctor")
    cd.Date = request.POST.get("date")
    cd.Message = request.POST.get("message")
    cd.save()
    return render(request,"index1.html")
