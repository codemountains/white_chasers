from django_filters import rest_framework as filters
from .models import Resort


class ResortFilter(filters.FilterSet):
	prefecture = filters.ChoiceFilter(
		choices=Resort.PREFECTURE,
		lookup_expr='exact'
	)
	name = filters.CharFilter(lookup_expr='contains')
	name_kana = filters.CharFilter(lookup_expr='contains')

	class Meta:
		model = Resort
		fields = [
			'prefecture',
			'name',
			'name_kana'
		]
