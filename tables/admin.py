from django.contrib import admin
from .models import ColdWaterTable, HotWaterTable, WarmTable, ElectricityTable, TemperatureTable

admin.site.register(ColdWaterTable)
admin.site.register(HotWaterTable)
admin.site.register(WarmTable)
admin.site.register(ElectricityTable)
admin.site.register(TemperatureTable)
