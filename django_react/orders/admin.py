from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "order_number",
        "price_usd",
        "srok_postavki",
        "price_rub",
    )
