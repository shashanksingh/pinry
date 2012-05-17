from django.contrib import admin
from .models import item , similarItems

class itemAdmin(admin.ModelAdmin):
   pass

class similarItemsAdmin(admin.ModelAdmin):
   pass      

admin.site.register(item , itemAdmin)
admin.site.register(similarItems , imilarItemsAdmin)

