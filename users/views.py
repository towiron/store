from django.shortcuts import render, redirect
from django.contrib import auth

from .models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm


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
	if request.method == 'POST':
		form = UserRegistrationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('users:login')

	else:
		form = UserRegistrationForm()
	context = {'form': form}
	return render(request, 'users/registration.html', context)



def profile(request):
	if request.method == 'POST':
		form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('users:profile')
		else:
			print(form.errors)
	else:
		form = UserProfileForm(instance=request.user)
	context = {'title': 'Store - Профиль', 'form': form}
	return render(request, 'users/profile.html', context)