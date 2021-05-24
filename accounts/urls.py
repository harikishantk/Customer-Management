from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('', views.home, name='home'),
    path('customers/<str:pk_test>', views.customers, name='customers'),
]
