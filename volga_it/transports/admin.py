from django.contrib import admin

from .models import Transports


@admin.register(Transports)
class TransportsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'model', 'color', 'identifier', 'latitude', 'longitude', 'minutePrice', 'dayPrice')
