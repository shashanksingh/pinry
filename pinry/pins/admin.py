from django.contrib import admin
from pinry.pins.models import Pin


class PinAdmin(admin.ModelAdmin):
   list_filter = ('author','similar_items',)
   search_fields = ['description','url',]
   list_display = ('url','blog_url_exists','buy_url_exists','similar_items','author','thumbnail',) 
admin.site.register(Pin,PinAdmin)


