from django.contrib import admin
from .models import Work, Episode


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'debut_at', 'published_at')
    list_display_links = list_display
    list_filter = ('type', )


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
