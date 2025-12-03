from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('cart/', views.cart, name='cart')
]   
