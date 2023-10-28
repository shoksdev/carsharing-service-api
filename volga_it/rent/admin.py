from django.contrib import admin

from .models import Rent


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    """Регистрируем модель Аренды в админ-панели, выводим некоторые поля"""
    list_display = ('transport', 'time_start', 'time_end', 'price_of_unit', 'price_type', 'final_price',)
