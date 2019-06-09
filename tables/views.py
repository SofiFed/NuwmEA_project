from django.contrib import admin
from .models import ColdWaterTable, HotWaterTable, WarmTable, ElectricityTable, TemperatureTable
from .forms import AddColdWaterTableDataForm, AddHotWaterTableDataForm, AddWarmTableDataForm, AddTemperatureTableDataForm, AddElectricityTableDataForm
from django.shortcuts import render
from django.shortcuts import redirect
import datetime
from managerusers.models import Manager 
from django.contrib.auth.models import User

def water(request):

	form1 = AddColdWaterTableDataForm(request.POST or None)
	datas = ColdWaterTable.objects.all()
	managers = Manager.objects.all()
	active_manager = False
	for manager in managers:
		if manager.manager_email == request.user.email:
			active_manager = manager.role == 1 and manager.is_staff
	errors = []
	message = ''
	if request.method == 'POST':
		if form1.is_valid():
			realdate = True
			if int(form1.cleaned_data['date_year']) == int(datetime.date.today().year) and int(form1.cleaned_data['date_month']) > int(datetime.date.today().month):
				realdate = False
		if form1.is_valid() and realdate:
			year = int(form1.cleaned_data['date_year'])
			month = int(form1.cleaned_data['date_month'])
			number = float(form1.cleaned_data['value'])
			building = int(form1.cleaned_data['building'])
			newdata = True
			for data in datas:
				if int(data.dateyear) == int(year) and int(data.datemonth) == int(month):
					newdata = False
					break;
			
			if newdata:
				if building == 1: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, ed_building1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 2: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, ed_building2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 3: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, ed_building4 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 4: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, ed_building5 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 5: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, ed_building6 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 6: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, ed_building7 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 7: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, garage = number, date=year*365+month*30 ); enterdata.save()
				elif building == 8: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, sport_building = number, date=year*365+month*30 ); enterdata.save()
				elif building == 9: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, canteen = number, date=year*365+month*30 ); enterdata.save()
				elif building == 10: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, hostel1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 11: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, hostel2 = number , date=year*365+month*30); enterdata.save()
				elif building == 12: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, hostel3 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 13: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, hostel4 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 14: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, hostel5 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 15: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, hostel6 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 16: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, hostel7 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 17: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, hostel8 = number , date=year*365+month*30); enterdata.save()
				elif building == 18: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, pavilion = number, date=year*365+month*30 ); enterdata.save()
				elif building == 19: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, car_fleet = number , date=year*365+month*30); enterdata.save()
				elif building == 20: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, boiler_house = number , date=year*365+month*30); enterdata.save()
				elif building == 21: enterdata = ColdWaterTable.objects.create(dateyear=year, datemonth=month, institute = number, date=year*365+month*30 ); enterdata.save()
			else:
				if building == 1: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(ed_building1 = number)
				elif building == 2: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2 = number )
				elif building == 3: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(ed_building4 = number )
				elif building == 4: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(ed_building5 = number )
				elif building == 5: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(ed_building6 = number )
				elif building == 6: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(ed_building7 = number )
				elif building == 7: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(garage = number )
				elif building == 8: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(sport_building = number )
				elif building == 9: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(canteen = number )
				elif building == 10: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel1 = number )
				elif building == 11: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel2 = number )
				elif building == 12: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel3 = number )
				elif building == 13: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel4 = number )
				elif building == 14: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel5 = number )
				elif building == 15: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel6 = number )
				elif building == 16: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel7 = number )
				elif building == 17: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel8 = number )
				elif building == 18: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(pavilion = number )
				elif building == 19: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(car_fleet = number )
				elif building == 20: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(boiler_house = number )
				elif building == 21: ColdWaterTable.objects.filter(dateyear=year, datemonth=month).update(institute = number )
				form1 = AddColdWaterTableDataForm()
			return redirect('water')
		else:
			if not realdate:
				message = "Обрано некоректну дату."
				errors.append("Оберіть дату правильно.")
	datas = ColdWaterTable.objects.all().order_by('-date')
	cols = [0]*21
	def cols_value(number,i):
		if number == None :
			cols[i] = cols[i] + 0
		else:
			cols[i] = cols[i] + number
	for data in datas:
		cols_value(data.ed_building1,0); cols_value(data.ed_building2,1); cols_value(data.ed_building4,2)
		cols_value(data.ed_building5,3); cols_value(data.ed_building6,4); cols_value(data.ed_building7,5)
		cols_value(data.garage,6); cols_value(data.sport_building,7); cols_value(data.canteen,8);
		cols_value(data.hostel1,9); cols_value(data.hostel2,10); cols_value(data.hostel3,11);
		cols_value(data.hostel4,12); cols_value(data.hostel5,13); cols_value(data.hostel6,14);
		cols_value(data.hostel7,15); cols_value(data.hostel8,16); cols_value(data.pavilion,17);
		cols_value(data.car_fleet,18); cols_value(data.boiler_house,19); cols_value(data.institute,20)

	return render(request, 'water.html', { 'form1' : form1, 'datas': datas, 'errors':errors, 'message':message, 'managers':managers, 'active_manager':active_manager, 'cols':cols,})
	

def hotwater(request):

	form1 = AddHotWaterTableDataForm(request.POST or None)
	datas = HotWaterTable.objects.all()
	managers = Manager.objects.all()
	active_manager = False
	for manager in managers:
		if manager.manager_email == request.user.email:
			active_manager = manager.role == 2 and manager.is_staff
	errors = []
	message = ''
	if request.method == 'POST':
		if form1.is_valid():
			realdate = True
			if int(form1.cleaned_data['date_year']) == int(datetime.date.today().year) and int(form1.cleaned_data['date_month']) > int(datetime.date.today().month):
				realdate = False
		if form1.is_valid() and realdate:
			year = int(form1.cleaned_data['date_year'])
			month = int(form1.cleaned_data['date_month'])
			number = float(form1.cleaned_data['value'])
			building = int(form1.cleaned_data['building'])
			newdata = True
			for data in datas:
				if int(data.dateyear) == int(year) and int(data.datemonth) == int(month):
					newdata = False
					break;
			
			if newdata:
				if building == 1: enterdata = HotWaterTable.objects.create(dateyear=year, datemonth=month, hostel7_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 2: enterdata = HotWaterTable.objects.create(dateyear=year, datemonth=month, hostel7_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 3: enterdata = HotWaterTable.objects.create(dateyear=year, datemonth=month, hostel8_1 = number , date=year*365+month*30); enterdata.save()
				elif building == 4: enterdata = HotWaterTable.objects.create(dateyear=year, datemonth=month, hostel8_2 = number , date=year*365+month*30); enterdata.save()
				
			else:
				if building == 1: HotWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel7_1 = number )
				elif building == 2: HotWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel7_2 = number )
				elif building == 3: HotWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel8_1 = number )
				elif building == 4: HotWaterTable.objects.filter(dateyear=year, datemonth=month).update(hostel8_2 = number )
				form1 = AddHotWaterTableDataForm()
			return redirect('hotwater')
		else:
			if not realdate:
				message = "Обрано некоректну дату."
				errors.append("Оберіть дату правильно.")
	datas = HotWaterTable.objects.all().order_by('-date')
	cols = [0]*4
	def cols_value(number,i):
		if number == None :
			cols[i] = cols[i] + 0
		else:
			cols[i] = cols[i] + number
	for data in datas:
		cols_value(data.hostel7_1,0); cols_value(data.hostel7_2,1); cols_value(data.hostel8_1,2); cols_value(data.hostel8_2,3)

	return render(request, 'hotwater.html', { 'form1' : form1, 'datas': datas, 'errors':errors, 'message':message, 'managers':managers, 'active_manager':active_manager, 'cols':cols,})
	

def warm(request):
	
	form1 = AddWarmTableDataForm(request.POST or None)
	datas = WarmTable.objects.all()
	managers = Manager.objects.all()
	active_manager = False
	for manager in managers:
		if manager.manager_email == request.user.email:
			active_manager = manager.role == 3 and manager.is_staff
	errors = []
	message = ''
	if request.method == 'POST':
		if form1.is_valid():
			realdate = True
			if int(form1.cleaned_data['date_year']) == int(datetime.date.today().year) and int(form1.cleaned_data['date_month']) > int(datetime.date.today().month):
				realdate = False
		if form1.is_valid() and realdate:
			year = int(form1.cleaned_data['date_year'])
			month = int(form1.cleaned_data['date_month'])
			number = float(form1.cleaned_data['value'])
			building = int(form1.cleaned_data['building'])
			newdata = True
			for data in datas:
				if int(data.dateyear) == int(year) and int(data.datemonth) == int(month):
					newdata = False
					break;
			
			if newdata:
				if building == 1: enterdata = WarmTable.objects.create(dateyear=year, datemonth=month, ed_building1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 2: enterdata = WarmTable.objects.create(dateyear=year, datemonth=month, hostel7 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 3: enterdata = WarmTable.objects.create(dateyear=year, datemonth=month, hostel8 = number , date=year*365+month*30); enterdata.save()
				elif building == 4: enterdata = WarmTable.objects.create(dateyear=year, datemonth=month, boiler_house = number , date=year*365+month*30); enterdata.save()
				elif building == 5: enterdata = WarmTable.objects.create(dateyear=year, datemonth=month, institute = number, date=year*365+month*30 ); enterdata.save()
			else:
				if building == 1: WarmTable.objects.filter(dateyear=year, datemonth=month).update(ed_building1 = number)
				elif building == 2: WarmTable.objects.filter(dateyear=year, datemonth=month).update(hostel7 = number )
				elif building == 3: WarmTable.objects.filter(dateyear=year, datemonth=month).update(hostel8 = number )
				elif building == 4: WarmTable.objects.filter(dateyear=year, datemonth=month).update(boiler_house = number )
				elif building == 5: WarmTable.objects.filter(dateyear=year, datemonth=month).update(institute = number )
				form1 = AddWarmTableDataForm()
			return redirect('warm')
		else:
			if not realdate:
				message = "Обрано некоректну дату."
				errors.append("Оберіть дату правильно.")
	datas = WarmTable.objects.all().order_by('-date')
	cols = [0]*5
	def cols_value(number,i):
		if number == None :
			cols[i] = cols[i] + 0
		else:
			cols[i] = cols[i] + number
	for data in datas:
		cols_value(data.ed_building1,0); cols_value(data.hostel7,1); cols_value(data.hostel8,2); cols_value(data.boiler_house,3);
		cols_value(data.institute,4)

	return render(request, 'warm.html', { 'form1' : form1, 'datas': datas, 'errors':errors, 'message':message, 'managers':managers, 'active_manager':active_manager, 'cols':cols,})
	


def electricity(request):

	form1 = AddElectricityTableDataForm(request.POST or None)
	datas = ElectricityTable.objects.all()
	managers = Manager.objects.all()
	active_manager = False
	for manager in managers:
		if manager.manager_email == request.user.email:
			active_manager = manager.role == 4 and manager.is_staff
	errors = []
	message = ''
	if request.method == 'POST':
		if form1.is_valid():
			realdate = True
			if int(form1.cleaned_data['date_year']) == int(datetime.date.today().year) and int(form1.cleaned_data['date_month']) > int(datetime.date.today().month):
				realdate = False
		if form1.is_valid() and realdate:
			year = int(form1.cleaned_data['date_year'])
			month = int(form1.cleaned_data['date_month'])
			number = float(form1.cleaned_data['value'])
			building = int(form1.cleaned_data['building'])
			newdata = True
			for data in datas:
				if int(data.dateyear) == int(year) and int(data.datemonth) == int(month):
					newdata = False
					break;
			
			if newdata:
				if building == 1: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building1_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 2: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building1_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 3: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building1_3 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 4: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 5: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 6: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2_3 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 7: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2_4= number, date=year*365+month*30 ); enterdata.save()
				elif building == 8: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2_5 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 9: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2_6 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 10: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2a_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 11: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2a_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 12: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2a_3 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 13: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2a_4= number, date=year*365+month*30 ); enterdata.save()
				elif building == 14: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2a_5 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 15: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building2a_6 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 16: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building6_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 17: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building6_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 18: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building6_3 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 19: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building6_4= number, date=year*365+month*30 ); enterdata.save()
				elif building == 20: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building7_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 21: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, ed_building7_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 22: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, barn = number, date=year*365+month*30 ); enterdata.save()
				elif building == 23: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, canteen = number, date=year*365+month*30 ); enterdata.save()
				elif building == 24: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, garage_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 25: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, garage_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 26: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, garage_3 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 27: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, proving_ground = number, date=year*365+month*30 ); enterdata.save()
				elif building == 28: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, pavilion = number, date=year*365+month*30 ); enterdata.save()
				elif building == 29: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 30: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel2 = number , date=year*365+month*30); enterdata.save()
				elif building == 31: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel3 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 32: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel4 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 33: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel5 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 34: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel6_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 35: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel6_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 36: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel7_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 37: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel7_2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 38: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel8_1 = number , date=year*365+month*30); enterdata.save()
				elif building == 39: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel8_2 = number , date=year*365+month*30); enterdata.save()
				elif building == 40: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, hostel8_3 = number , date=year*365+month*30); enterdata.save()
				elif building == 41: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, TP38_1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 42: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, TP38_2 = number , date=year*365+month*30); enterdata.save()
				elif building == 43: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, TP38_3 = number , date=year*365+month*30); enterdata.save()
				elif building == 44: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, TP72_1 = number , date=year*365+month*30); enterdata.save()
				elif building == 45: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, TP72_2 = number , date=year*365+month*30); enterdata.save()
				elif building == 46: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, TP72_3 = number , date=year*365+month*30); enterdata.save()
				elif building == 47: enterdata = ElectricityTable.objects.create(dateyear=year, datemonth=month, institute = number, date=year*365+month*30 ); enterdata.save()
			else:
				if building == 1: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building1_1 = number)
				elif building == 2: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building1_2 = number )
				elif building == 3: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building1_3 = number )
				elif building == 4: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2_1 = number )
				elif building == 5: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2_2 = number )
				elif building == 6: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2_3 = number )
				elif building == 7: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2_4 = number )
				elif building == 8: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2_5 = number )
				elif building == 9: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2_6 = number )
				elif building == 10: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2a_1 = number )
				elif building == 11: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2a_2 = number )
				elif building == 12: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2a_3 = number )
				elif building == 13: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2a_4 = number )
				elif building == 14: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2a_5 = number )
				elif building == 15: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2a_6 = number )
				elif building == 16: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building6_1 = number )
				elif building == 17: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building6_2 = number )
				elif building == 18: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building6_3 = number )
				elif building == 19: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building6_4 = number )
				elif building == 20: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building7_1 = number )
				elif building == 21: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(ed_building7_2 = number )
				elif building == 22: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(barn = number )
				elif building == 23: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(canteen = number )
				elif building == 24: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(garage_1 = number )
				elif building == 25: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(garage_2 = number )
				elif building == 26: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(garage_3 = number )
				elif building == 27: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(proving_ground = number )
				elif building == 28: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(pavilion = number )
				elif building == 29: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel1 = number )			
				elif building == 30: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel2 = number )
				elif building == 31: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel3 = number )
				elif building == 32: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel4 = number )
				elif building == 33: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel5 = number )
				elif building == 34: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel6_1 = number )
				elif building == 35: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel6_2 = number )
				elif building == 36: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel7_1 = number )
				elif building == 37: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel7_2 = number )
				elif building == 38: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel8_1 = number )
				elif building == 39: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel8_2 = number )
				elif building == 40: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(hostel8_3 = number )
				elif building == 41: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(TP38_1 = number )
				elif building == 42: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(TP38_2 = number )
				elif building == 43: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(TP38_3 = number )
				elif building == 44: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(TP72_1 = number )
				elif building == 45: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(TP72_2 = number )
				elif building == 46: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(TP72_3 = number )
				elif building == 47: ElectricityTable.objects.filter(dateyear=year, datemonth=month).update(institute = number )
				form1 = AddElectricityTableDataForm()
			return redirect('electricity')
		else:
			if not realdate:
				message = "Обрано некоректну дату."
				errors.append("Оберіть дату правильно.")
	datas = ElectricityTable.objects.all().order_by('-date')
	cols = [0]*47
	def cols_value(number,i):
		if number == None :
			cols[i] = cols[i] + 0
		else:
			cols[i] = cols[i] + number
	for data in datas:
		cols_value(data.ed_building1_1,0); cols_value(data.ed_building1_2,1); cols_value(data.ed_building1_3,2)
		cols_value(data.ed_building2_1,3); cols_value(data.ed_building2_2,4); cols_value(data.ed_building2_3,5)
		cols_value(data.ed_building2_4,6); cols_value(data.ed_building2_5,7); cols_value(data.ed_building2_6,8)
		cols_value(data.ed_building2a_1,9); cols_value(data.ed_building2a_2,10); cols_value(data.ed_building2a_3,11)
		cols_value(data.ed_building2a_4,12); cols_value(data.ed_building2a_5,13); cols_value(data.ed_building2a_6,14)
		cols_value(data.ed_building6_1,15); cols_value(data.ed_building6_2,16); cols_value(data.ed_building6_3,17)
		cols_value(data.ed_building6_4,18); cols_value(data.ed_building7_1,19); cols_value(data.ed_building7_2,20)
		cols_value(data.barn,21); cols_value(data.canteen,22); cols_value(data.garage_1,23)
		cols_value(data.garage_2,24); cols_value(data.garage_3,25); cols_value(data.proving_ground,26);cols_value(data.pavilion,27); 
		cols_value(data.hostel1,28); cols_value(data.hostel2,29); cols_value(data.hostel3,30) 
		cols_value(data.hostel4,31); cols_value(data.hostel5,32); cols_value(data.hostel6_1,33)
		cols_value(data.hostel6_2,34); cols_value(data.hostel7_1,35); cols_value(data.hostel7_2,36)
		cols_value(data.hostel8_1,37); cols_value(data.hostel8_2,38); cols_value(data.hostel8_3,39)
		cols_value(data.TP38_1,40); cols_value(data.TP38_2,41); cols_value(data.TP38_3,42)
		cols_value(data.TP72_1,43); cols_value(data.TP72_2,44); cols_value(data.TP72_3,45)
		cols_value(data.institute,46)

	return render(request, 'energy.html', { 'form1' : form1, 'datas': datas, 'errors':errors, 'message':message, 'managers':managers, 'active_manager':active_manager, 'cols':cols,})
	

def temperature(request):

	form1 = AddTemperatureTableDataForm(request.POST or None)
	datas = TemperatureTable.objects.all()
	managers = Manager.objects.all()
	active_manager = False
	for manager in managers:
		if manager.manager_email == request.user.email:
			active_manager = manager.role == 5 and manager.is_staff
	errors = []
	message = ''
	if request.method == 'POST':
		if form1.is_valid():
			realdate = True
			if int(form1.cleaned_data['date_year']) == int(datetime.date.today().year) and int(form1.cleaned_data['date_month']) > int(datetime.date.today().month):
				realdate = False
		if form1.is_valid() and realdate:
			year = int(form1.cleaned_data['date_year'])
			month = int(form1.cleaned_data['date_month'])
			number = float(form1.cleaned_data['value'])
			building = int(form1.cleaned_data['building'])
			newdata = True
			for data in datas:
				if int(data.dateyear) == int(year) and int(data.datemonth) == int(month):
					newdata = False
					break;
			
			if newdata:
				if building == 1: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, ed_building1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 2: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, ed_building2 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 3: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, ed_building4 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 4: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, ed_building5 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 5: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, ed_building6 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 6: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, ed_building7 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 7: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, garage = number, date=year*365+month*30 ); enterdata.save()
				elif building == 8: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, sport_building = number, date=year*365+month*30 ); enterdata.save()
				elif building == 9: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, canteen = number, date=year*365+month*30 ); enterdata.save()
				elif building == 10: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, hostel1 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 11: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, hostel2 = number , date=year*365+month*30); enterdata.save()
				elif building == 12: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, hostel3 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 13: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, hostel4 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 14: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, hostel5 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 15: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, hostel6 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 16: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, hostel7 = number, date=year*365+month*30 ); enterdata.save()
				elif building == 17: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, hostel8 = number , date=year*365+month*30); enterdata.save()
				elif building == 18: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, pavilion = number, date=year*365+month*30 ); enterdata.save()
				elif building == 19: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, car_fleet = number , date=year*365+month*30); enterdata.save()
				elif building == 20: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, boiler_house = number , date=year*365+month*30); enterdata.save()
				elif building == 21: enterdata = TemperatureTable.objects.create(dateyear=year, datemonth=month, institute = number, date=year*365+month*30 ); enterdata.save()
			else:
				if building == 1: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(ed_building1 = number)
				elif building == 2: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(ed_building2 = number )
				elif building == 3: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(ed_building4 = number )
				elif building == 4: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(ed_building5 = number )
				elif building == 5: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(ed_building6 = number )
				elif building == 6: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(ed_building7 = number )
				elif building == 7: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(garage = number )
				elif building == 8: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(sport_building = number )
				elif building == 9: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(canteen = number )
				elif building == 10: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(hostel1 = number )
				elif building == 11: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(hostel2 = number )
				elif building == 12: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(hostel3 = number )
				elif building == 13: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(hostel4 = number )
				elif building == 14: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(hostel5 = number )
				elif building == 15: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(hostel6 = number )
				elif building == 16: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(hostel7 = number )
				elif building == 17: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(hostel8 = number )
				elif building == 18: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(pavilion = number )
				elif building == 19: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(car_fleet = number )
				elif building == 20: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(boiler_house = number )
				elif building == 21: TemperatureTable.objects.filter(dateyear=year, datemonth=month).update(institute = number )
				form1 = AddTemperatureTableDataForm()
			return redirect('temperature')
		else:
			if not realdate:
				message = "Обрано некоректну дату."
				errors.append("Оберіть дату правильно.")
	datas = TemperatureTable.objects.all().order_by('-date')
	cols = [0]*21
	count = 0
	def cols_value(number,i):
		if number == None :
			cols[i] = cols[i] + 0
		else:
			cols[i] = cols[i] + number
	for data in datas:
		cols_value(data.ed_building1,0); cols_value(data.ed_building2,1); cols_value(data.ed_building4,2)
		cols_value(data.ed_building5,3); cols_value(data.ed_building6,4); cols_value(data.ed_building7,5)
		cols_value(data.garage,6); cols_value(data.sport_building,7); cols_value(data.canteen,8);
		cols_value(data.hostel1,9); cols_value(data.hostel2,10); cols_value(data.hostel3,11);
		cols_value(data.hostel4,12); cols_value(data.hostel5,13); cols_value(data.hostel6,14);
		cols_value(data.hostel7,15); cols_value(data.hostel8,16); cols_value(data.pavilion,17);
		cols_value(data.car_fleet,18); cols_value(data.boiler_house,19); cols_value(data.institute,20)
		count = count + 1

	if count != 0 :
		for i in range(21):
			cols[i] = cols[i] / float(count)

	return render(request, 'temperature.html', { 'form1' : form1, 'datas': datas, 'errors':errors, 'message':message, 'managers':managers, 'active_manager':active_manager, 'cols':cols,})
	

