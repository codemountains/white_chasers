from rest_framework import serializers
from .models import Forecast, ForecastDetail
from utils.formaters import fmt_forecasted_at
from datetime import timedelta


class ForecastDetailSerializer(serializers.ModelSerializer):
	forecasted_at = fmt_forecasted_at()
	forecasted_date = serializers.SerializerMethodField()
	forecasted_time = serializers.SerializerMethodField()
	temp = serializers.SerializerMethodField()
	wind_speed = serializers.SerializerMethodField()
	wind_deg_name = serializers.SerializerMethodField()
	pop = serializers.SerializerMethodField()
	rain = serializers.SerializerMethodField()
	snow = serializers.SerializerMethodField()
	snow_depth = serializers.SerializerMethodField()
	sys = serializers.SerializerMethodField()

	class Meta:
		model = ForecastDetail
		fields = [
			'id',
			'forecast',
			'forecasted_at',
			'forecasted_date',
			'forecasted_time',
			'temp',
			'feels_like',
			'temp_min',
			'temp_max',
			'pressure',
			'sea_level',
			'grnd_level',
			'humidity',
			'temp_kf',
			'weather',
			'weather_id',
			'weather_description',
			'weather_icon_name',
			'clouds',
			'wind_speed',
			'wind_deg',
			'wind_deg_name',
			'visibility',
			'pop',
			'rain',
			'snow',
			'snow_depth',
			'sys'
		]

	def get_forecasted_date(self, obj):
		return (obj.forecasted_at + timedelta(hours=9)).date()

	def get_forecasted_time(self, obj):
		return (obj.forecasted_at + timedelta(hours=9)).time()

	def get_temp(self, obj):
		return str(round(obj.temp, 2))

	def get_wind_speed(self, obj):
		return str(round(obj.wind_speed, 1))

	def get_wind_deg_name(self, obj):
		if 11 <= obj.wind_deg < 30:
			deg_name = '北北東'
		elif 30 <= obj.wind_deg < 61:
			deg_name = '北東'
		elif 61 <= obj.wind_deg < 80:
			deg_name = '東北東'
		elif 80 <= obj.wind_deg < 101:
			deg_name = '東'
		elif 101 <= obj.wind_deg < 120:
			deg_name = '東南東'
		elif 120 <= obj.wind_deg < 151:
			deg_name = '東南'
		elif 151 <= obj.wind_deg < 170:
			deg_name = '南南東'
		elif 170 <= obj.wind_deg < 191:
			deg_name = '南'
		elif 191 <= obj.wind_deg < 210:
			deg_name = '南南西'
		elif 210 <= obj.wind_deg < 241:
			deg_name = '南西'
		elif 241 <= obj.wind_deg < 260:
			deg_name = '西南西'
		elif 260 <= obj.wind_deg < 281:
			deg_name = '西'
		elif 281 <= obj.wind_deg < 300:
			deg_name = '西北西'
		elif 300 <= obj.wind_deg < 331:
			deg_name = '北西'
		elif 331 <= obj.wind_deg < 350:
			deg_name = '北北西'
		elif 350 <= obj.wind_deg:
			deg_name = '北'
		else:
			deg_name = '北'

		return deg_name

	def get_pop(self, obj):
		return str(round(round(obj.pop, 2) * 100))

	def get_rain(self, obj):
		if obj.rain is not None:
			return str(round(obj.rain, 2))
		else:
			return obj.rain

	def get_snow(self, obj):
		if obj.snow is not None:
			return str(round(obj.snow, 2))
		else:
			return obj.snow

	def get_snow_depth(self, obj):
		if obj.snow is not None:
			return str(round(obj.snow * 1, 1))
		else:
			return None

	def get_sys(self, obj):
		if obj.sys == 'd':
			return 'day'
		else:
			return 'night'


class ForecastSerializer(serializers.ModelSerializer):
	forecast_details = ForecastDetailSerializer(many=True, read_only=True)

	class Meta:
		model = Forecast
		fields = [
			'id',
			'resort',
			'forecast_details'
		]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['forecast_details'] = sorted(
			response['forecast_details'],
			key=lambda x: x['forecasted_at']
		)
		return response
