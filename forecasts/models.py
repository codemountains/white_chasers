import uuid
from django.db import models
from resorts.models import Resort


class Forecast(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_at = models.DateTimeField(auto_now=True)
	resort = models.ForeignKey(
		Resort,
		related_name='resort_forecast',
		on_delete=models.CASCADE
	)
	weather = models.JSONField(blank=True, null=True)

	def __str__(self):
		return '{0} ({1})'.format(str(self.resort), str(self.created_at))


class ForecastDetail(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_at = models.DateTimeField(auto_now=True)
	forecast = models.ForeignKey(
		Forecast,
		related_name='forecast_details',
		on_delete=models.CASCADE
	)
	forecasted_at = models.DateTimeField(auto_now=False)
	temp = models.DecimalField(
		max_digits=7,
		decimal_places=3
	)
	feels_like = models.DecimalField(
		max_digits=7,
		decimal_places=3
	)
	temp_min = models.DecimalField(
		max_digits=7,
		decimal_places=3
	)
	temp_max = models.DecimalField(
		max_digits=7,
		decimal_places=3
	)
	pressure = models.IntegerField()
	sea_level = models.IntegerField()
	grnd_level = models.IntegerField()
	humidity = models.IntegerField()
	temp_kf = models.IntegerField()
	weather = models.CharField(max_length=50)
	weather_id = models.IntegerField()
	weather_description = models.CharField(max_length=200)
	weather_icon_name = models.CharField(max_length=10)
	clouds = models.IntegerField()
	wind_speed = models.DecimalField(
		max_digits=7,
		decimal_places=3
	)
	wind_deg = models.IntegerField()
	visibility = models.IntegerField()
	pop = models.DecimalField(
		max_digits=7,
		decimal_places=3
	)
	rain = models.DecimalField(
		blank=True,
		null=True,
		max_digits=7,
		decimal_places=3
	)
	snow = models.DecimalField(
		blank=True,
		null=True,
		max_digits=7,
		decimal_places=3
	)
	sys = models.CharField(max_length=1)

	def __str__(self):
		return str(self.forecast)
