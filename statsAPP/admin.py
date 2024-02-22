from django.contrib import admin
from .models import *

class ClubAdmin(admin.ModelAdmin):
    list_display = ('nom', 'murabbiy', 'davlat')
    search_fields = ['nom']
    list_filter = ['davlat']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('ism', 'club', 'narx', 'davlat')
    search_fields = ['nom']
    list_filter = ['club']
    autocomplete_fields = ['club']

admin.site.register(Davlat)
admin.site.register(Club,ClubAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(Transfer)
