from django.urls import path
from . import views

app_name = 'SalesManager'
urlpatterns = [
    path('', views.StorageView.as_view(), name='storage'),
    path('<int:pk>/product/', views.ProductView.as_view(), name='product'),
    path('<int:pk>/action/', views.StorageActionView.as_view(), name='action'),
    path('<int:pk>/item/', views.ItemView.as_view(), name='item'),
]