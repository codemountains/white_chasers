from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Forecast, ForecastDetail
from .serializers import ForecastSerializer
from white_chasers import settings
from datetime import datetime, timedelta
from django.utils import timezone
import requests


class ForecastViewSet(viewsets.ModelViewSet):
	serializer_class = ForecastSerializer
	queryset = Forecast.objects.all()
	permission_classes = (AllowAny,)
	pagination_class = None

	def perform_create(self, serializer):
		resort = serializer.validated_data.get('resort')

		url = settings.URL_OPEN_WEATHER_MAP
		query = {
			'lat': resort.latitude,
			'lon': resort.longitude,
			'cnt': '40',
			'lang': 'ja',
			'units': 'metric',
			'appid': settings.OPEN_WEATHER_MAP_APP_ID
		}
		response = requests.get(url, params=query)
		json_list = response.json()['list']

		forecast = serializer.save(weather=json_list)

		for index in range(response.json()['cnt']):
			json_item = json_list[index]

			json_dt_txt = datetime.strptime(json_item['dt_txt'], '%Y-%m-%d %H:%M:%S')
			forecasted_at = timezone.make_aware(
				json_dt_txt + timedelta(hours=9),
				timezone.get_default_timezone()
			)

			rain = None
			json_rain = json_item.get('rain')
			if json_rain is not None:
				rain = json_rain['3h']

			snow = None
			json_snow = json_item.get('snow')
			if json_snow is not None:
				snow = json_snow['3h']

			detail = ForecastDetail(
				forecast=forecast,
				forecasted_at=forecasted_at,
				temp=json_item['main']['temp'],
				feels_like=json_item['main']['feels_like'],
				temp_min=json_item['main']['temp_min'],
				temp_max=json_item['main']['temp_max'],
				pressure=json_item['main']['pressure'],
				sea_level=json_item['main']['sea_level'],
				grnd_level=json_item['main']['grnd_level'],
				humidity=json_item['main']['humidity'],
				temp_kf=json_item['main']['temp_kf'],
				weather=json_item['weather'][0]['main'],
				weather_id=json_item['weather'][0]['id'],
				weather_description=json_item['weather'][0]['description'],
				weather_icon_name=json_item['weather'][0]['icon'],
				clouds=json_item['clouds']['all'],
				wind_speed=json_item['wind']['speed'],
				wind_deg=json_item['wind']['deg'],
				visibility=json_item['visibility'],
				pop=json_item['pop'],
				rain=rain,
				snow=snow,
				sys=json_item['sys']['pod']
			)
			detail.save()
