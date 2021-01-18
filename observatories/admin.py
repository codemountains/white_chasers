from django.contrib import admin
from .models import Observatory, Rainfall, Snowfall, SnowDepth, Temperature


admin.site.register(Observatory)
admin.site.register(Rainfall)
admin.site.register(Snowfall)
admin.site.register(SnowDepth)
admin.site.register(Temperature)
