from django.contrib import admin
from django.urls import include, path

from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    #path('', include('products.urls')),
]
