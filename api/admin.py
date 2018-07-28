from django.contrib import admin

from .models import Screenplay

class ScreenplayAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year', 'writer')
    list_filter = ('year',)
    ordering = ('-title',)

admin.site.register(Screenplay, ScreenplayAdmin)
