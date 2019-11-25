from django.db import models
from django.utils import timezone


class Storage(models.Model):
    now = timezone.now()
    creation_date = models.DateTimeField('creation date', default=now)
    last_edition = models.DateTimeField('edition date', default=now)


class StorageAction(models.Model):
    now = timezone.now()
    name = models.CharField(max_length=200)
    date = models.DateTimeField('creation date', default=now)
    action_date = models.DateTimeField('real date', default=now)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    type = models.CharField(max_length=8, default='Purchase')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    purchase_date = models.DateTimeField('date of purchase')
    sale_date = models.DateTimeField('date of sold', blank=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    batch_code = models.CharField(max_length=10, blank=True)
    storage_action = models.ForeignKey(StorageAction, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=purchase_price)
    producer_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

