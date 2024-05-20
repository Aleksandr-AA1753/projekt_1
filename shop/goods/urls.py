from django.contrib import admin
from django.urls import path

from . import views
admin.site.site_header = "Страница управления"

app_name = 'goods'
urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),

]