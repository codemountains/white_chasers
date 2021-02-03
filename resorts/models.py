import uuid
from django.db import models
from utils import choices


class Resort(models.Model):
	PREFECTURE = choices.PREFECTURE

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	name = models.CharField(max_length=100)
	name_kana = models.CharField(max_length=200, blank=True, null=True)
	postal_code = models.CharField(max_length=8, blank=True, null=True)
	prefecture = models.IntegerField(choices=PREFECTURE)
	address = models.CharField(max_length=200, blank=True, null=True)
	latitude = models.DecimalField(
		max_digits=9,
		decimal_places=6,
		blank=True,
		null=True
	)
	longitude = models.DecimalField(
		max_digits=9,
		decimal_places=6,
		blank=True,
		null=True
	)
	url = models.URLField(blank=True, null=True)
	live_camera_url = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name


class BrowsingHistory(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_at = models.DateTimeField(auto_now=True)
	resort = models.ForeignKey(
		Resort,
		related_name='resort_browsing_history',
		on_delete=models.CASCADE
	)

	class Meta:
		verbose_name_plural = 'Browsing Histories'

	def __str__(self):
		str_created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
		return '{0} - {1}'.format(str_created_at, str(self.resort))
