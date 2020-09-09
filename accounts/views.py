from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import CreateUserForm,UserProfileInfoForm


# Create your views here.

def home(request):
	context = {}
	return render(request,"accounts/home.html",context)

def staffPage(request):
	context = {}
	return render(request,"accounts/staff.html",context)

def LogPage(request):
	context = {}
	return render(request,"accounts/log.html",context)

def AboutPage(request):
	context = {}
	return render(request,"accounts/about.html",context)

def RegisterPage(request):
	if request.user.is_authenticated:
		return redirect("dashboard")

	else:	
		form = CreateUserForm()
		if request.method =="POST":
			form = CreateUserForm(request.POST)
			if User.objects.filter(username=request.POST.get("username")).exists() and User.objects.filter(email=request.POST.get("email")).exists():
				messages.info(request,"You have already been registered! Please,login with your credentials")
			elif User.objects.filter(username=request.POST.get("username")).exists():
				messages.warning(request,"The given username is already in use.Please,choose another one ")

			elif User.objects.filter(email=request.POST.get("email")).exists():
				messages.warning(request,"The given email is already registered")

			else:

				if form.is_valid():
					user = form.save()

					Profile.objects.create(user = user,first_name = user.username)

					username = form.cleaned_data.get("username")
					messages.success(request,"Account has been successfully created for "+username)
					return redirect("login")

				else:
					messages.error(request,"Please follow the given instructions while setting the Password")

	context = {"form":form}
	return render(request,"accounts/register.html",context)

def LoginPage(request):
	if request.user.is_authenticated:
		return redirect("dashboard")

	else:
		if request.method == "POST":
			username = request.POST.get("Username")
			password = request.POST.get("Password")
			user_auth = authenticate(request,username=username,password=password)
			if user_auth is not None:
				login(request,user_auth)
				return redirect("home")
			else:
				messages.error(request,"Username or Password is incorrect")

	context = {}
	return render(request,"accounts/login.html",context)

@login_required
def LogOutUser(request):
	logout(request)
	return redirect("home")

@login_required
def ProfileUpdate(request):
	info = request.user.profile
	form = UserProfileInfoForm(instance = info)
	if request.method == "POST":
		form = UserProfileInfoForm(request.POST,request.FILES,instance = info)
		if form.is_valid():
			form.save()
			return redirect("dashboard")
	context = {"form":form}
	return render(request,"accounts/profile_update.html",context)


@login_required
def Dashboard(request):
	username = request.user.username
	email = request.user.email
	phone = request.user.profile.phone
	f_name = request.user.profile.first_name 
	l_name = request.user.profile.last_name
	context = {"username":username,"email":email,"phone_no":phone,"firstname":f_name,"lastname":l_name,}
	return render(request,"accounts/dashboard.html",context)