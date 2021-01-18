from rest_framework.pagination import PageNumberPagination


class ResortPagination(PageNumberPagination):
	page_query_param = 'page'
	last_page_strings = ('last',)
	page_size = 50
	max_page_size = 50

