from django.contrib import admin
from .models import Forecast, ForecastDetail

admin.site.register(Forecast)
admin.site.register(ForecastDetail)
