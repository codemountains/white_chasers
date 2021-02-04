from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import MeasuredObservatorySerializer
from .models import Observatory, Snowfall
from .paginations import ObservatoryPagination
from .filters import ObservatoryFilter
from resorts.models import Resort


def get_observatory_list(lat, lon, dist):
	queryset = Observatory.objects.raw("""
	SELECT
	*,
	(
		6371
		* acos(
		  cos(radians(%%s))
		  * cos(radians(latitude))
		  * cos(radians(longitude) - radians(%%s))
		  + sin(radians(%%s))
		  * sin(radians(latitude))
		) 
	) AS distance
	FROM %(observatory_table)s
	INNER JOIN %(snowfall_table)s
	ON %(observatory_table)s.id = %(snowfall_table)s.observatory_id
	WHERE (
		6371
		* acos(
		  cos(radians(%%s))
		  * cos(radians(latitude))
		  * cos(radians(longitude) - radians(%%s))
		  + sin(radians(%%s))
		  * sin(radians(latitude))
		) 
	) < %%s
	ORDER BY distance
	""" % {
		'observatory_table': Observatory._meta.db_table,
		'snowfall_table': Snowfall._meta.db_table
	}, [lat, lon, lat, lat, lon, lat, dist])
	return queryset


def get_observatory_retrieve(lat, lon, observatory_id):
	queryset = Observatory.objects.raw("""
	SELECT
	*,
	(
		6371
		* acos(
		  cos(radians(%%s))
		  * cos(radians(latitude))
		  * cos(radians(longitude) - radians(%%s))
		  + sin(radians(%%s))
		  * sin(radians(latitude))
		) 
	) AS distance
	FROM %(observatory_table)s
	INNER JOIN %(snowfall_table)s
	ON %(observatory_table)s.id = %(snowfall_table)s.observatory_id
	WHERE %(observatory_table)s.id = %%s
	""" % {
		'observatory_table': Observatory._meta.db_table,
		'snowfall_table': Snowfall._meta.db_table
	}, [lat, lon, lat, observatory_id.hex])
	return queryset


class ObservatoryViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = MeasuredObservatorySerializer
	queryset = Observatory.objects.filter(
		observatory_snowfall__isnull=False
	).order_by('code')
	permission_classes = (AllowAny,)
	pagination_class = ObservatoryPagination
	filter_class = ObservatoryFilter

	def list(self, request, *args, **kwargs):
		resort_id = self.request.query_params.get('resort')
		resort = Resort.objects.filter(id=resort_id).first()
		dist = self.request.query_params.get('dist')
		if dist is None:
			dist = '30'

		if resort is not None:
			queryset = get_observatory_list(
				str(resort.latitude),
				str(resort.longitude),
				dist
			)
			paginate_queryset = self.paginate_queryset(queryset)
			serializer = MeasuredObservatorySerializer(paginate_queryset, many=True)
			return self.get_paginated_response(serializer.data)
		else:
			paginate_queryset = self.paginate_queryset(self.queryset)
			serializer = MeasuredObservatorySerializer(paginate_queryset, many=True)
			return self.get_paginated_response(serializer.data)

	def retrieve(self, request, *args, **kwargs):
		observatory_id = self.kwargs.get('pk')
		observatory = Observatory.objects.get(id=observatory_id)

		if observatory is None:
			response = {
				'message': '該当のアメダス観測所がありません'
			}
			return Response(response, status=status.HTTP_400_BAD_REQUEST)

		resort_id = self.request.query_params.get('resort')
		resort = Resort.objects.filter(id=resort_id).first()
		if resort is not None:
			queryset = get_observatory_retrieve(
				str(resort.latitude),
				str(resort.longitude),
				observatory.id
			)
			serializer = MeasuredObservatorySerializer(queryset, many=True)
			return Response(serializer.data)
		else:
			queryset = Observatory.objects.filter(id=observatory_id)
			serializer = MeasuredObservatorySerializer(queryset, many=True)
			return Response(serializer.data)
