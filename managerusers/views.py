from django.contrib.auth.models import User
from .forms import AddManagerUserForm
from .models import Manager

from django.shortcuts import redirect
from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

def AddManagerUser(request):
	form = AddManagerUserForm(request.POST or None)
	Role = ['Холодна вода', 'Гаряча вода', 'Тепло', 'Електроенергія', 'Температура']
	managers = Manager.objects.all().order_by('manager_email')
	users = User.objects.all()
	errors = []
	message = ''
	if request.method == 'POST':
		unique_email = True
		unique_role = True
		if form.is_valid():
			for manager in managers:
				if str(manager.manager_email) == str(form.cleaned_data['manager_email']):
					unique_email = False
				if int(manager.role) == int(form.cleaned_data['role']):
					unique_role = False
		if form.is_valid() and form.cleaned_data['manager_email'].endswith('@nuwm.edu.ua') and unique_email and unique_role:
			manager_email = form.cleaned_data['manager_email']
			role = form.cleaned_data['role']

			manageruser = Manager.objects.create(manager_email=manager_email, role=role)
			manageruser.save()
			r=int(form.cleaned_data['role']) - 1
			email_message = "Вас авторизовано на веб-сервісі NuwmEnergyAnalitics у ролі Енергоменеджера. Для контролю доступна таблиця " + Role[r]
			send_mail('Авторизація NuwmEnergyAnalitics', email_message, settings.EMAIL_HOST_USER, [manager_email])

			return redirect('profile')

		else:
			if not form.cleaned_data['manager_email'].endswith('@nuwm.edu.ua'):
				message = 'Користувач не був доданий до списку Енергоменеджерів.'
				errors.append('Ви можете додати користувача лише з доменом @nuwm.edu.ua')
			if not unique_email:
				message = 'Користувач не був доданий до списку Енергоменеджерів.'
				errors.append('У списку уже є Енергоменеджер з цією електронною адресою. Для внесення змін видаліть попереднього Енергоменеджера зі списку.')
			if not unique_role:
				message = 'Користувач не був доданий до списку Енергоменеджерів.'
				errors.append('У списку уже є Енергоменеджер, який відповідає за цю таблицю. Для внесення змін видаліть попереднього Енергоменеджера зі списку.')
		form = AddManagerUserForm()
	return render(request, 'account.html', { 'form' : form, 'managers':managers, 'users':users, 'errors':errors, 'message':message, 'admin':settings.EMAIL_HOST_USER, })

def DelManagerUser(request):
	form = AddManagerUserForm(request.POST or None)
	if request.method == 'POST':
		managers = Manager.objects.all()
		m_role = int(request.POST.get('m_role')) 
		manageruser = Manager.objects.get(role=m_role)
		email_message = "Ви були видалені зі списку Енергоменеджерів на NuwmEnergyAnalitics. Для отримання прав доступу зверніться до Адміністратора " + str(settings.EMAIL_HOST_USER)
		send_mail('NuwmEnergyAnalitics', email_message, settings.EMAIL_HOST_USER, [manageruser.manager_email])
		manageruser.delete()
	return redirect('profile')

def ActiveManagerRole(request):
	Role = ['Холодна вода', 'Гаряча вода', 'Тепло', 'Електроенергія', 'Температура']
	if request.method == 'POST':
		m_role = int(request.POST.get('m_role')) 
		manageruser = Manager.objects.get(role=m_role)
		Manager.objects.filter(role=m_role).update(is_staff=True)
		email_message = "Вам відкрито доступ до таблиці " + Role[m_role-1] + " на NuwmEnergyAnalitics."
		send_mail('NuwmEnergyAnalitics', email_message, settings.EMAIL_HOST_USER, [manageruser.manager_email])
	return redirect('profile')

def DeactiveManagerRole(request):
	Role = ['Холодна вода', 'Гаряча вода', 'Тепло', 'Електроенергія', 'Температура']
	if request.method == 'POST':
		m_role = int(request.POST.get('m_role')) 
		manageruser = Manager.objects.get(role=m_role)
		Manager.objects.filter(role=m_role).update(is_staff=False)
		email_message = "Вам обмежено доступ до таблиці " + Role[m_role-1] + " на NuwmEnergyAnalitics. Для отримання прав доступу зверніться до Адміністратора " + str(settings.EMAIL_HOST_USER)
		send_mail('NuwmEnergyAnalitics', email_message, settings.EMAIL_HOST_USER, [manageruser.manager_email])
	return redirect('profile')


	





