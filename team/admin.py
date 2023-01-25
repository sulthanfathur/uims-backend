from django.contrib import admin
from .models import TeamMember

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'division',
        'sub_division',
        'jabatan',
    ]
    list_filter = [
        'division',
        'sub_division',
        'jabatan',
    ]
admin.site.register(TeamMember, TeamMemberAdmin)
