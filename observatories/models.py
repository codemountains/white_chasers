import uuid
from django.db import models
from utils import choices


class Observatory(models.Model):
	"""
	アメダス観測所
	"""
	PREFECTURE = choices.PREFECTURE

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	name = models.CharField(max_length=100)
	name_kana = models.CharField(max_length=200)
	code = models.IntegerField()
	observation_type = models.CharField(max_length=4)
	prefecture = models.IntegerField(choices=PREFECTURE)
	location = models.CharField(max_length=100)
	latitude = models.DecimalField(
		max_digits=9,
		decimal_places=6
	)
	longitude = models.DecimalField(
		max_digits=9,
		decimal_places=6
	)

	class Meta:
		verbose_name_plural = 'Observatories'

	def __str__(self):
		return '{0} - {1}'.format(str(self.code), self.name)


class Rainfall(models.Model):
	"""
	降水量情報（降水量全要素）
	https://www.data.jma.go.jp/obd/stats/data/mdrr/docs/csv_dl_format_preall.html
	"""
	QUALITY_LEVEL = choices.QUALITY_LEVEL

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	updated_at = models.DateTimeField(auto_now=True)
	observatory = models.OneToOneField(
		Observatory,
		related_name='observatory_rainfall',
		on_delete=models.CASCADE
	)
	observed_at = models.DateTimeField(auto_now=False)
	rainfall_3h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	rainfall_3h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	rainfall_6h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	rainfall_6h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	rainfall_12h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	rainfall_12h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	rainfall_24h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	rainfall_24h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	rainfall_48h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	rainfall_48h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	rainfall_72h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	rainfall_72h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)

	def __str__(self):
		return str(self.observatory)


class Snowfall(models.Model):
	"""
	降雪量情報（降雪量全要素）
	https://www.data.jma.go.jp/obd/stats/data/mdrr/docs/csv_dl_format_sndall.html
	"""
	QUALITY_LEVEL = choices.QUALITY_LEVEL

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	updated_at = models.DateTimeField(auto_now=True)
	observatory = models.OneToOneField(
		Observatory,
		related_name='observatory_snowfall',
		on_delete=models.CASCADE
	)
	observed_at = models.DateTimeField(auto_now=False)
	snowfall_3h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	snowfall_3h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	snowfall_6h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	snowfall_6h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	snowfall_12h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	snowfall_12h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	snowfall_24h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	snowfall_24h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	snowfall_48h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	snowfall_48h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	snowfall_72h = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	snowfall_72h_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)

	def __str__(self):
		return str(self.observatory)


class SnowDepth(models.Model):
	"""
	現在の積雪深
	https://www.data.jma.go.jp/obd/stats/data/mdrr/docs/csv_dl_format_snc.html
	"""
	QUALITY_LEVEL = choices.QUALITY_LEVEL

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	updated_at = models.DateTimeField(auto_now=True)
	observatory = models.OneToOneField(
		Observatory,
		related_name='observatory_snow_depth',
		on_delete=models.CASCADE
	)
	observed_at = models.DateTimeField(auto_now=False)
	snow_depth = models.IntegerField(
		blank=True,
		null=True
	)
	snow_depth_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	ratio_compared_to_normal = models.IntegerField(
		blank=True,
		null=True
	)

	def __str__(self):
		return str(self.observatory)


class Temperature(models.Model):
	"""
	最高気温
	https://www.data.jma.go.jp/obd/stats/data/mdrr/docs/csv_dl_format_mxtem.html
	最低気温
	https://www.data.jma.go.jp/obd/stats/data/mdrr/docs/csv_dl_format_mntem.html
	"""
	QUALITY_LEVEL = choices.QUALITY_LEVEL

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	updated_at = models.DateTimeField(auto_now=True)
	observatory = models.OneToOneField(
		Observatory,
		related_name='observatory_temperature',
		on_delete=models.CASCADE
	)
	observed_at = models.DateTimeField(auto_now=False)
	highest = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	highest_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	highest_observed_at = models.DateTimeField(auto_now=False)
	lowest = models.DecimalField(
		blank=True,
		null=True,
		max_digits=4,
		decimal_places=1
	)
	lowest_quality_level = models.IntegerField(
		blank=True,
		null=True,
		choices=QUALITY_LEVEL
	)
	lowest_observed_at = models.DateTimeField(auto_now=False)

	def __str__(self):
		return str(self.observatory)
