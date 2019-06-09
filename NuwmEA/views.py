from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from managerusers.models import Manager


def home(request):
	managers = Manager.objects.all()
	if request.user.is_authenticated:
		status = False
		for manager in managers:
			if request.user.is_superuser or str(manager.manager_email) == str(request.user.email):
				status = True
				active_manager = manager
		if status and active_manager.is_staff:
			return render(request, 'home.html', {'active_manager':active_manager,})
		elif request.user.is_superuser:
			return render(request, 'home.html')
		else:
			return redirect('login')
	else:
		return redirect('login')




