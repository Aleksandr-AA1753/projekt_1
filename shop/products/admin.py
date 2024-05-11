from django.contrib import admin

from products.models import General
from products.models import Fridge


admin.site.register(General)
admin.site.register(Fridge)