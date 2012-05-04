from django.contrib import admin
from pinry.pins.models import Pin


class PinAdmin(admin.ModelAdmin):
   pass
admin.site.register(Pin,PinAdmin)


