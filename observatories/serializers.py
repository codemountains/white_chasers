from rest_framework import serializers
from decimal import Decimal, ROUND_HALF_UP
from .models import Observatory, Rainfall, Snowfall, SnowDepth, Temperature
from utils.formaters import fmt_updated_at, fmt_observed_at


class RainfallSerializer(serializers.ModelSerializer):
	updated_at = fmt_updated_at()
	observed_at = fmt_observed_at()

	class Meta:
		model = Rainfall
		fields = [
			'id',
			'updated_at',
			'observatory',
			'observed_at',
			'rainfall_3h',
			'rainfall_6h',
			'rainfall_12h',
			'rainfall_24h',
			'rainfall_48h',
			'rainfall_72h'
		]


class SnowfallSerializer(serializers.ModelSerializer):
	updated_at = fmt_updated_at()
	observed_at = fmt_observed_at()

	class Meta:
		model = Snowfall
		fields = [
			'id',
			'updated_at',
			'observatory',
			'observed_at',
			'snowfall_3h',
			'snowfall_6h',
			'snowfall_12h',
			'snowfall_24h',
			'snowfall_48h',
			'snowfall_72h'
		]


class SnowDepthSerializer(serializers.ModelSerializer):
	updated_at = fmt_updated_at()
	observed_at = fmt_observed_at()

	class Meta:
		model = SnowDepth
		fields = [
			'id',
			'updated_at',
			'observatory',
			'observed_at',
			'snow_depth'
		]


class TemperatureSerializer(serializers.ModelSerializer):
	updated_at = fmt_updated_at()
	observed_at = fmt_observed_at()
	highest_observed_at = fmt_observed_at()
	lowest_observed_at = fmt_observed_at()

	class Meta:
		model = Temperature
		fields = [
			'id',
			'updated_at',
			'observatory',
			'observed_at',
			'highest',
			'highest_observed_at',
			'lowest',
			'lowest_observed_at'
		]


class ObservatorySerializer(serializers.ModelSerializer):
	prefecture_name = serializers.CharField(
		source='get_prefecture_display',
		read_only=True
	)
	observatory_rainfall = RainfallSerializer(many=False, read_only=True)
	observatory_snowfall = SnowfallSerializer(many=False, read_only=True)
	observatory_snow_depth = SnowDepthSerializer(many=False, read_only=True)
	observatory_temperature = TemperatureSerializer(many=False, read_only=True)

	class Meta:
		model = Observatory
		fields = [
			'id',
			'name',
			'name_kana',
			'code',
			'observation_type',
			'prefecture',
			'prefecture_name',
			'location',
			'latitude',
			'longitude',
			'observatory_rainfall',
			'observatory_snowfall',
			'observatory_snow_depth',
			'observatory_temperature'
		]


class MeasuredObservatorySerializer(serializers.ModelSerializer):
	prefecture_name = serializers.CharField(
		source='get_prefecture_display',
		read_only=True
	)
	distance = serializers.SerializerMethodField()
	observatory_rainfall = RainfallSerializer(many=False, read_only=True)
	observatory_snowfall = SnowfallSerializer(many=False, read_only=True)
	observatory_snow_depth = SnowDepthSerializer(many=False, read_only=True)
	observatory_temperature = TemperatureSerializer(many=False, read_only=True)

	class Meta:
		model = Observatory
		fields = [
			'id',
			'name',
			'name_kana',
			'code',
			'observation_type',
			'prefecture',
			'prefecture_name',
			'location',
			'latitude',
			'longitude',
			'distance',
			'observatory_rainfall',
			'observatory_snowfall',
			'observatory_snow_depth',
			'observatory_temperature'
		]

	def get_distance(self, obj):
		if hasattr(obj, 'distance'):
			dist = str(obj.distance)
			dist_decimal = Decimal(dist).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
			return str(dist_decimal)
		else:
			return None
