from django.views import generic
from .models import *


class StorageView(generic.ListView):
    template_name = 'SalesManager/storage.html'
    context_object_name = 'storage_items'

    def get_queryset(self):
        storage = Storage.objects.get(id=1)
        products = storage.products.order_by('purchase_date')
        actions = storage.actions.order_by('date')
        return products, actions


class ProductView(generic.DetailView):
    model = Product
    template_name = 'SalesManager/product.html'

    def get_queryset(self):
        storage = Storage.objects.get(id=1)
        item = storage.items.get(products)


class StorageActionView(generic.DetailView):
    model = StorageAction
    template_name = 'SalesManager/storageAction.html'


class ItemView(generic.DeleteView):
    model = Item
    template_name = 'SalesManager/Item.html'
