from django.contrib import admin
from django.urls import path

from carts import views


app_name = 'carts'
urlpatterns = [
    path('cart_add/<slug:product_slug>/', views.cart_add, name='cart_add'), #Добавить
    path('cart_change/<slug:product_slug>/', views.cart_change, name='cart_change'), #Изменить
    path('cart_remove/<slug:product_slug>/', views.cart_remove, name='cart_remove'), #Удалить
]