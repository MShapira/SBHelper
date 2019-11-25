from django.urls import path
from . import views

app_name = 'SalesManager'
urlpatterns = [
    path('', views.StorageView.as_view(), name='storage'),
    path('<int:pk>/products/', views.ProductView.as_view(), name='product'),
    path('<int:pk>/actions/', views.StorageActionView.as_view(), name='action'),
    path('actions/', views.StorageActionsView.as_view(), name='actions'),
]