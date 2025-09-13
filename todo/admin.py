from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=(
        'task',
        'is_completed',
        'priority',
        'updated_at',
    )
    list_filter = ('priority', 'is_completed',)
    search_fields = ('task',)

admin.site.register(Task, TaskAdmin)