from django.contrib import admin

from .models import *

class AuditorAdmin(admin.ModelAdmin):
    list_display = ('name', 'corpus', 'places', 'tables', 'microphones', 'speakers', 'computers', 'proektor', 'interactiveBoard')
    # list_display_links = ('corpus')
    search_fields = ('name', 'corpus', 'places', 'tables', 'microphones', 'speakers', 'computers', 'proektor', 'interactiveBoard')

class BronAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'allowed', 'date', 'auditor', 'start_time', 'end_time')
    list_display_links = ('id', 'auditor')
    search_fields = ('user', 'date', 'allowed', 'auditor', 'date', 'start_time', 'end_time')
    list_editable = ('allowed', 'date', 'start_time', 'end_time')

admin.site.register(Auditor, AuditorAdmin)
admin.site.register(Bron, BronAdmin)
admin.site.register(Corpus)
