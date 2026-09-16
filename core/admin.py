from django.contrib import admin
from .models import ContentItem


@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "created_at",
    )

    list_filter = (
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "text",
    )

    ordering = (
        "-created_at",
    )