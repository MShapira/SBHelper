from django.db import models
from django.utils import timezone


class Storage(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    last_edition = models.DateTimeField('edition date', auto_now=True)

    def __str__(self):
        return self.name


class StorageAction(models.Model):
    now = timezone.now()
    name = models.CharField(max_length=200)
    date = models.DateTimeField('creation date', auto_now_add=True)
    action_date = models.DateTimeField('real date', default=now)
    storage = models.ForeignKey(to=Storage, related_name="actions", on_delete=models.CASCADE)
    type = models.CharField(max_length=8, default='Purchase')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    purchase_date = models.DateTimeField('date of purchase')
    sale_date = models.DateTimeField('date of sold', blank=True, null=True)
    storage = models.ForeignKey(to=Storage, related_name="products", on_delete=models.CASCADE)
    batch_code = models.CharField(max_length=10, blank=True, null=True)
    storage_action = models.ForeignKey(to=StorageAction, related_name="products", on_delete=models.CASCADE, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=purchase_price, blank=True, null=True)
    producer_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


