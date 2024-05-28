from django.contrib import admin
from django.urls import path

from carts import views


app_name = 'carts'
urlpatterns = [
    path('cart_add/', views.cart_add, name='cart_add'), #Добавить
    path('cart_change/', views.cart_change, name='cart_change'), #Изменить
    path('cart_remove', views.cart_remove, name='cart_remove'), #Удалить
]