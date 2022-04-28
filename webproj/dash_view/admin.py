from django.contrib import admin

# Register your models here.
from dash_view.models import DetectedItem


class DetectedItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'timestamp', 'confidence', 'filename')


admin.site.register(DetectedItem, DetectedItemAdmin)
