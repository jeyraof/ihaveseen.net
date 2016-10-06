from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'model', 'tid', 'action', 'old_value', 'new_value', 'created_at', ]
    list_display_links = list_display
    list_filter = ['model', 'action', ]
    search_fields = ['user__username', 'user__email', 'model', 'tid', 'action', ]

