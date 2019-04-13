from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Table, CustomUser
from .serializers import TableSerializer, CustomUserSerializer
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

class TableView(viewsets.ModelViewSet):
	queryset = Table.objects.all()
	serializer_class = TableSerializer

class CustomUserView(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer

def user_login(request):
	context = {}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect(reverse('home'))
		else:
			context["error"] = "Provide valid credentials !!"
			return render(request, "registration/login.html", context)
	else:
		return render(request, "registration/login.html", context)

def home(request):
	context = {}
	context['user'] = request.user
	return render(request, "home.html", context)

def user_logout(request):
	if request.method == "POST":
		logout(request)
		return HttpResponseRedirect(reverse('user_login'))



