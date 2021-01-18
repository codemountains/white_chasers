from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.ResortViewSet)

measurement_router = routers.DefaultRouter()
measurement_router.register('', views.MeasuredResortViewSet)

option_router = routers.DefaultRouter()
option_router.register('', views.ResortOptionViewSet)

urlpatterns = [
	path(
		'browsing/',
		views.BrowsingHistoryCreateViewSet.as_view(),
		name='browsing'
	),
	path('options/', include(option_router.urls)),
	path('measurements/', include(measurement_router.urls)),
	path('', include(router.urls)),
]
