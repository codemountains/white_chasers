from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authen/', include('djoser.urls.jwt')),
    path('api/v1/resorts/', include('resorts.urls')),
    path('api/v1/observatories/', include('observatories.urls')),
    path('api/v1/forecasts/resorts/', include('forecasts.urls')),
]
