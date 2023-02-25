from django.shortcuts import render, redirect
from django.contrib import auth

from .models import User
from .forms import UserLoginForm


def login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user:
				auth.login(request, user)
				return redirect('index')
	else:
		form = UserLoginForm()
	context = {'form': form}
	return render(request, 'users/login.html', context)



def registration(request):
	return render(request, 'users/registration.html')