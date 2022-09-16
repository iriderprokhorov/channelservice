from django.db import models


class Order(models.Model):
    number = models.PositiveIntegerField()
    order_number = models.PositiveIntegerField()
    price_usd = models.PositiveIntegerField()
    srok_postavki = models.DateField()
    price_rub = models.FloatField()
