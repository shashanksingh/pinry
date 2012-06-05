from django.contrib import admin
from .models import similarItems


class similarItemsAdmin(admin.ModelAdmin):
   list_filter = ('pins',)
   search_fields = ['name',]
   list_display = ('name','pins','page_url',)      

admin.site.register(similarItems , similarItemsAdmin)

