from django.contrib import admin
from .models import *

class SponsorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'brand',
        'division',
        'image',
    ]
    list_filter = ('division',)
admin.site.register(Sponsor, SponsorAdmin)
