from rest_framework.pagination import PageNumberPagination


class ObservatoryPagination(PageNumberPagination):
	page_query_param = 'page'
	last_page_strings = ('last',)
	page_size = 20
	max_page_size = 20
