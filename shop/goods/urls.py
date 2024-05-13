from django.contrib import admin
from django.urls import path

from . import views
admin.site.site_header = "Страница управления"

app_name = 'goods'
urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),

]