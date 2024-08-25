from django.contrib import admin
from .models import Viand, ViandType


@admin.register(Viand)
class ViandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "type",
        "available",
    )
    list_filter = (
        "type__name",
        "available",
    )
    search_fields = (
        "name",
        "ingredients",
    )


@admin.register(ViandType)
class ViandTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "available",
    )
    list_filter = ("available",)
    search_fields = ("name",)
