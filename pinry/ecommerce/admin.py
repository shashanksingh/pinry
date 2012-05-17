from django.contrib import admin
from .models import product , similarItems

class productAdmin(admin.ModelAdmin):
   pass

class similarItemsAdmin(admin.ModelAdmin):
   pass      

admin.site.register(product , productAdmin)
admin.site.register(similarItems , similarItemsAdmin)

