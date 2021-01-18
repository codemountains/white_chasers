from django_filters import rest_framework as filters
from .models import Observatory


class ObservatoryFilter(filters.FilterSet):
	prefecture = filters.ChoiceFilter(
		choices=Observatory.PREFECTURE,
		lookup_expr='exact'
	)
	name = filters.CharFilter(lookup_expr='contains')
	name_kana = filters.CharFilter(lookup_expr='contains')
	location = filters.CharFilter(lookup_expr='contains')
	latitude = filters.NumberFilter(lookup_expr='contains')
	longitude = filters.NumberFilter(lookup_expr='contains')

	class Meta:
		model = Observatory
		fields = [
			'prefecture',
			'name',
			'name_kana',
			'location',
			'latitude',
			'longitude'
		]
