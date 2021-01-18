from django.db.models import Q
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ResortSerializer, MeasuredResortSerializer, \
	ResortOptionSerializer, BrowsingHistorySerializer
from .models import Resort, BrowsingHistory
from .filters import ResortFilter
from .paginations import ResortPagination
from observatories.models import Observatory
import jaconv


def get_measured_resort_list(lat, lon, dist):
	queryset = Resort.objects.raw("""
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
	FROM %(resort_table)s
	HAVING distance < %%s
	ORDER BY distance, prefecture, name_kana
	""" % {
		'resort_table': Resort._meta.db_table
	}, [lat, lon, lat, dist])
	return queryset


def get_measured_resort_retrieve(lat, lon, resort_id):
	queryset = Resort.objects.raw("""
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
	FROM %(resort_table)s
	WHERE %(resort_table)s.id = %%s
	ORDER BY distance, prefecture, name_kana
	""" % {
		'resort_table': Resort._meta.db_table
	}, [lat, lon, lat, resort_id.hex])
	return queryset


class ResortViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = ResortSerializer
	queryset = Resort.objects.all().order_by('prefecture', 'name_kana')
	permission_classes = (AllowAny,)
	filter_class = ResortFilter
	pagination_class = ResortPagination

	def get_queryset(self):
		param = self.request.query_params.get('key')
		if param is not None:
			conv_param = jaconv.normalize(param, 'NFKC')
			conv_param = jaconv.hira2kata(conv_param)
			conv_param = jaconv.h2z(conv_param, ascii=True, digit=False)
			kana = jaconv.alphabet2kana(param)
			conv_kana = jaconv.hira2kata(kana)
			queryset = Resort.objects.filter(
				Q(name__icontains=param)
				| Q(name__icontains=conv_param)
				| Q(name__icontains=conv_kana)
				| Q(name_kana__icontains=param)
				| Q(name_kana__icontains=conv_param)
				| Q(name_kana__icontains=conv_kana)
			).order_by('prefecture', 'name_kana')
			return queryset
		else:
			return self.queryset


class MeasuredResortViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = MeasuredResortSerializer
	queryset = Resort.objects.all().order_by('prefecture', 'name_kana')
	permission_classes = (AllowAny,)
	filter_class = ResortFilter
	pagination_class = ResortPagination

	def list(self, request, *args, **kwargs):
		obs_id = self.request.query_params.get('obs')
		observatory = Observatory.objects.filter(id=obs_id).first()
		dist = self.request.query_params.get('dist')
		if dist is None:
			dist = '30'

		if observatory is not None:
			queryset = get_measured_resort_list(
				str(observatory.latitude),
				str(observatory.longitude),
				dist
			)
			paginate_queryset = self.paginate_queryset(queryset)
			serializer = MeasuredResortSerializer(paginate_queryset, many=True)
			return self.get_paginated_response(serializer.data)
		else:
			paginate_queryset = self.paginate_queryset(self.queryset)
			serializer = MeasuredResortSerializer(paginate_queryset, many=True)
			return self.get_paginated_response(serializer.data)

	def retrieve(self, request, *args, **kwargs):
		resort_id = self.kwargs.get('pk')
		resort = Resort.objects.get(id=resort_id)
		if resort is None:
			response = {
				'message': '該当のスキー場がありません'
			}
			return Response(response, status=status.HTTP_400_BAD_REQUEST)

		obs_id = self.request.query_params.get('obs')
		observatory = Observatory.objects.filter(id=obs_id).first()

		if observatory is not None:
			queryset = get_measured_resort_retrieve(
				str(observatory.latitude),
				str(observatory.longitude),
				resort.id
			)
			serializer = MeasuredResortSerializer(queryset, many=True)
			return Response(serializer.data)
		else:
			queryset = Resort.objects.filter(id=resort_id)
			serializer = MeasuredResortSerializer(queryset, many=True)
			return Response(serializer.data)


class ResortOptionViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = ResortOptionSerializer
	queryset = Resort.objects.all().order_by('prefecture', 'name_kana')
	permission_classes = (AllowAny,)
	filter_class = ResortFilter
	pagination_class = None


class BrowsingHistoryCreateViewSet(generics.CreateAPIView):
	serializer_class = BrowsingHistorySerializer
	queryset = BrowsingHistory.objects.all()
	permission_classes = (AllowAny,)
	pagination_class = None
