from django.contrib import admin

from references.models import ReferencesManufacturer
from references.models import ReferencesColour
from references.models import ReferencesProduct_type


admin.site.register(ReferencesManufacturer)
admin.site.register(ReferencesColour)
admin.site.register(ReferencesProduct_type)
