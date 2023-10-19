from django.contrib import admin

from .models import Transports

admin.site.register(Transports)


class TransportsAdmin(admin.ModelAdmin):
    list_display = ('model', 'color', 'identifier', 'latitude', 'longitude', 'minutePrice', 'dayPrice')
