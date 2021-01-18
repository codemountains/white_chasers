import io
import requests
import pandas as pd
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from decimal import Decimal
from datetime import datetime, timedelta
from white_chasers import settings
from observatories.models import Observatory, Rainfall, \
	Snowfall, SnowDepth, Temperature


CSV_SEP = ','
ENCODE_SHIFT_JIS = 'shift_jis'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def fmt_datetime(year, month, day, hour, minute, second='00'):
	if hour == '24':
		dt_str = '{0}-{1}-{2} {3}:{4}:{5}'.format(
			year, month, day, '00', minute, second
		)
		dt = datetime.strptime(dt_str, DATETIME_FORMAT) + timedelta(days=1)
		return datetime.strftime(dt, DATETIME_FORMAT)

	return '{0}-{1}-{2} {3}:{4}:{5}'.format(
		year, month, day, hour, minute, second
	)


def get_rainfall():
	response = requests.get(settings.URL_RAINFALL_ALL_CSV)
	df = pd.read_csv(
		io.BytesIO(response.content),
		sep=CSV_SEP,
		encoding=ENCODE_SHIFT_JIS,
		dtype=object
	).fillna(0)

	for index, row in df.iterrows():
		rf = Rainfall.objects.filter(observatory__code=row[0]).first()

		dt = fmt_datetime(row[4], row[5], row[6], row[7], row[8])
		observed_at = make_aware(datetime.strptime(dt, DATETIME_FORMAT))

		if rf is None:
			observatory = Observatory.objects.filter(code=int(row[0])).first()
			if observatory is not None:
				new_rf = Rainfall(
					observatory=observatory,
					observed_at=observed_at,
					rainfall_3h=Decimal(row[21]),
					rainfall_3h_quality_level=int(row[22]),
					rainfall_6h=Decimal(row[25]),
					rainfall_6h_quality_level=int(row[26]),
					rainfall_12h=Decimal(row[29]),
					rainfall_12h_quality_level=int(row[30]),
					rainfall_24h=Decimal(row[33]),
					rainfall_24h_quality_level=int(row[34]),
					rainfall_48h=Decimal(row[37]),
					rainfall_48h_quality_level=int(row[38]),
					rainfall_72h=Decimal(row[41]),
					rainfall_72h_quality_level=int(row[42])
				)
				new_rf.save()
		else:
			rf.observed_at = observed_at
			rf.rainfall_3h = Decimal(row[21])
			rf.rainfall_3h_quality_level = int(row[22])
			rf.rainfall_6h = Decimal(row[25])
			rf.rainfall_6h_quality_level = int(row[26])
			rf.rainfall_12h = Decimal(row[29])
			rf.rainfall_12h_quality_level = int(row[30])
			rf.rainfall_24h = Decimal(row[33])
			rf.rainfall_24h_quality_level = int(row[34])
			rf.rainfall_48h = Decimal(row[37])
			rf.rainfall_48h_quality_level = int(row[38])
			rf.rainfall_72h = Decimal(row[41])
			rf.rainfall_72h_quality_level = int(row[42])
			rf.save()


def get_snowfall():
	response = requests.get(settings.URL_SNOWFALL_ALL_CSV)
	df = pd.read_csv(
		io.BytesIO(response.content),
		sep=CSV_SEP,
		encoding=ENCODE_SHIFT_JIS,
		dtype=object
	).fillna(0)

	for index, row in df.iterrows():
		sf = Snowfall.objects.filter(observatory__code=row[0]).first()

		dt = fmt_datetime(row[4], row[5], row[6], row[7], row[8])
		observed_at = make_aware(datetime.strptime(dt, DATETIME_FORMAT))

		if sf is None:
			observatory = Observatory.objects.filter(
				code=int(row[0])
			).first()
			if observatory is not None:
				new_sf = Snowfall(
					observatory=observatory,
					observed_at=observed_at,
					snowfall_3h=Decimal(row[21]),
					snowfall_3h_quality_level=int(row[22]),
					snowfall_6h=Decimal(row[25]),
					snowfall_6h_quality_level=int(row[26]),
					snowfall_12h=Decimal(row[29]),
					snowfall_12h_quality_level=int(row[30]),
					snowfall_24h=Decimal(row[33]),
					snowfall_24h_quality_level=int(row[34]),
					snowfall_48h=Decimal(row[37]),
					snowfall_48h_quality_level=int(row[38]),
					snowfall_72h=Decimal(row[41]),
					snowfall_72h_quality_level=int(row[42])
				)
				new_sf.save()
		else:
			sf.observed_at = observed_at
			sf.snowfall_3h = Decimal(row[21])
			sf.snowfall_3h_quality_level = int(row[22])
			sf.snowfall_6h = Decimal(row[25])
			sf.snowfall_6h_quality_level = int(row[26])
			sf.snowfall_12h = Decimal(row[29])
			sf.snowfall_12h_quality_level = int(row[30])
			sf.snowfall_24h = Decimal(row[33])
			sf.snowfall_24h_quality_level = int(row[34])
			sf.snowfall_48h = Decimal(row[37])
			sf.snowfall_48h_quality_level = int(row[38])
			sf.snowfall_72h = Decimal(row[41])
			sf.snowfall_72h_quality_level = int(row[42])
			sf.save()


def get_snow_depths():
	response = requests.get(settings.URL_SNOW_DEPTH_CSV)

	df = pd.read_csv(
		io.BytesIO(response.content),
		sep=CSV_SEP,
		encoding=ENCODE_SHIFT_JIS,
		dtype=object
	).fillna(0)

	for index, row in df.iterrows():
		sd = SnowDepth.objects.filter(observatory__code=row[0]).first()

		dt = fmt_datetime(row[4], row[5], row[6], row[7], row[8])
		observed_at = make_aware(datetime.strptime(dt, DATETIME_FORMAT))

		if sd is None:
			observatory = Observatory.objects.filter(
				code=int(row[0])
			).first()
			if observatory is not None:
				new_sd = SnowDepth(
					observatory=observatory,
					observed_at=observed_at,
					snow_depth=int(row[9]),
					snow_depth_quality_level=int(row[10]),
					ratio_compared_to_normal=int(row[11]),
				)
				new_sd.save()
		else:
			sd.observed_at = observed_at
			sd.snow_depth = int(row[9])
			sd.snow_depth_quality_level = int(row[10])
			sd.ratio_compared_to_normal = int(row[11])
			sd.save()


def get_temperature():
	response_highest = requests.get(settings.URL_HIGHEST_TEMP_CSV)
	df_highest = pd.read_csv(
		io.BytesIO(response_highest.content),
		sep=CSV_SEP,
		encoding=ENCODE_SHIFT_JIS,
		dtype=object
	).fillna(0)

	response_lowest = requests.get(settings.URL_LOWEST_TEMP_CSV)
	df_lowest = pd.read_csv(
		io.BytesIO(response_lowest.content),
		sep=CSV_SEP,
		encoding=ENCODE_SHIFT_JIS,
		dtype=object
	).fillna(0)

	for index_highest, row_highest in df_highest.iterrows():
		for index_lowest, row_lowest in df_lowest.iterrows():
			if row_highest[0] == row_lowest[0]:
				temp = Temperature.objects.filter(observatory__code=row_highest[0]).first()

				dt = fmt_datetime(
					row_highest[4],
					row_highest[5],
					row_highest[6],
					row_highest[7],
					row_highest[8]
				)
				observed_at = make_aware(
					datetime.strptime(dt, DATETIME_FORMAT)
				)

				highest_dt = fmt_datetime(
					row_highest[4],
					row_highest[5],
					row_highest[6],
					row_highest[11],
					row_highest[12]
				)
				highest_observed_at = make_aware(
					datetime.strptime(highest_dt, DATETIME_FORMAT)
				)

				lowest_dt = fmt_datetime(
					row_lowest[4],
					row_lowest[5],
					row_lowest[6],
					row_lowest[11],
					row_lowest[12]
				)
				lowest_observed_at = make_aware(
					datetime.strptime(lowest_dt, DATETIME_FORMAT)
				)

				if temp is None:
					observatory = Observatory.objects.filter(code=int(row_highest[0])).first()
					if observatory is not None:
						tp = Temperature(
							observatory=observatory,
							observed_at=observed_at,
							highest=Decimal(row_highest[9]),
							highest_quality_level=int(row_highest[10]),
							highest_observed_at=highest_observed_at,
							lowest=Decimal(row_lowest[9]),
							lowest_quality_level=int(row_lowest[10]),
							lowest_observed_at=lowest_observed_at
						)
						tp.save()
				else:
					temp.observed_at = observed_at
					temp.highest = Decimal(row_highest[9])
					temp.highest_quality_level = int(row_highest[10])
					temp.highest_observed_at = highest_observed_at
					temp.lowest = Decimal(row_lowest[9])
					temp.lowest_quality_level = int(row_lowest[10])
					temp.lowest_observed_at = lowest_observed_at
					temp.save()


class Command(BaseCommand):
	def handle(self, *args, **options):
		get_rainfall()
		get_snowfall()
		get_snow_depths()
		get_temperature()
