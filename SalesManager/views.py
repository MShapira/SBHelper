from django.views import generic
from .models import *


class StorageView(generic.ListView):
    template_name = 'SalesManager/storage.html'
    context_object_name = 'storage_items'

    def get_queryset(self):
        return Storage.objects.get(Product).order_by('date of purchase')


class ProductView(generic.DetailView):
    model = Product
    template_name = 'SalesManager/product.html'


class StorageActionView(generic.DetailView):
    model = StorageAction
    template_name = 'SalesManager/storageAction.html'


class StorageActionsView(generic.ListView):
    template_name = 'SalesManager/storageActions.html'
    context_object_name = 'storage_actions'

    def get_queryset(self):
        return Storage.objects.get(StorageAction).order_by('creation date')