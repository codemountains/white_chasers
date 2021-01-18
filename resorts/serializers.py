from rest_framework import serializers
from decimal import Decimal, ROUND_HALF_UP
from .models import Resort, BrowsingHistory
import jaconv


class ResortSerializer(serializers.ModelSerializer):
	prefecture_name = serializers.CharField(
		source='get_prefecture_display',
		read_only=True
	)

	class Meta:
		model = Resort
		fields = [
			'id',
			'name',
			'name_kana',
			'postal_code',
			'prefecture',
			'prefecture_name',
			'address',
			'latitude',
			'longitude',
			'url',
			'live_camera_url'
		]


class MeasuredResortSerializer(serializers.ModelSerializer):
	prefecture_name = serializers.CharField(
		source='get_prefecture_display',
		read_only=True
	)
	distance = serializers.SerializerMethodField()

	class Meta:
		model = Resort
		fields = [
			'id',
			'name',
			'name_kana',
			'postal_code',
			'prefecture',
			'prefecture_name',
			'address',
			'latitude',
			'longitude',
			'url',
			'live_camera_url',
			'distance'
		]

	def get_distance(self, obj):
		if hasattr(obj, 'distance'):
			dist = str(obj.distance)
			dist_decimal = Decimal(dist).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
			return str(dist_decimal)
		else:
			return None


class ResortOptionSerializer(serializers.ModelSerializer):
	prefecture_name = serializers.CharField(
		source='get_prefecture_display',
		read_only=True
	)
	name_hiragana = serializers.SerializerMethodField()

	class Meta:
		model = Resort
		fields = [
			'id',
			'name',
			'name_kana',
			'name_hiragana',
			'prefecture',
			'prefecture_name',
		]

	def get_name_hiragana(self, obj):
		return jaconv.kata2hira(obj.name)


class BrowsingHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = BrowsingHistory
		fields = [
			'resort'
		]
