from django import forms
from .models import Manager

class AddManagerUserForm(forms.Form):

	COLDWATER_MANAGER = 1
	HOTWATER_MANAGER = 2
	WARM_MANAGER = 3
	ELECTRICITY_MANAGER = 4
	TEMPERATURE_MANAGER = 5
	ROLES = (
	    (COLDWATER_MANAGER, 'Холодна вода'),
	    (HOTWATER_MANAGER, 'Гаряча вода'),
	    (WARM_MANAGER, 'Тепло'),
	    (ELECTRICITY_MANAGER, 'Електроенергія'),
	    (TEMPERATURE_MANAGER, 'Температура'),
	)
	manager_email = forms.EmailField(label='Введіть e-mail користувача ', max_length=300, widget=forms.TextInput, required=True)
	role = forms.ChoiceField(label='Оберіть роль для користувача ', choices=ROLES, widget=forms.RadioSelect)





