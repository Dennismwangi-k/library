from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from .forms import NewUserForm
from .forms import AddcontactForm
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('home-after-login')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"login.html", context={"login_form":form})

def home_after_login(request):
    return render(request, "home-after-login.html")

def contact(request):
    form = AddcontactForm()
    if request.method == 'POST':
        form = AddcontactForm(request.POST)
        if form.is_valid():
            contactform= form.save(commit=False)
            contactform.save()
            return redirect('contact')
        else:
            messages.error(request, 'an error occurred during registration')

            
    context = {
        'form': form
    }
    return render(request, "contact-us.html", context)

def profile(request):
    return render(request, "student-profile.html")