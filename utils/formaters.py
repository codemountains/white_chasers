from rest_framework import serializers


DATETIME_FORMAT = '%Y-%m-%d %H:%M'
DATE_FORMAT = '%Y-%m-%d'


def fmt_created_at():
	formatted_created_at = serializers.DateTimeField(
		format=DATETIME_FORMAT,
		read_only=True
	)
	return formatted_created_at


def fmt_updated_at():
	formatted_updated_at = serializers.DateTimeField(
		format=DATETIME_FORMAT,
		read_only=True
	)
	return formatted_updated_at


def fmt_observed_at():
	formatted_observed_at = serializers.DateTimeField(
		format=DATETIME_FORMAT,
		read_only=True
	)
	return formatted_observed_at


def fmt_forecasted_at():
	formatted_forecasted_at = serializers.DateTimeField(
		format=DATETIME_FORMAT,
		read_only=True
	)
	return formatted_forecasted_at


def fmt_forecasted_date():
	formatted_forecasted_date = serializers.DateField(
		format=DATE_FORMAT,
		read_only=True
	)
	return formatted_forecasted_date
