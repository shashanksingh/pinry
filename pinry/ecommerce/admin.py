from django.contrib import admin
from .models import similarItems


class similarItemsAdmin(admin.ModelAdmin):
   pass      

admin.site.register(similarItems , similarItemsAdmin)

