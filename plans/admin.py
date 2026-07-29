from django.contrib import admin
from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "plan_type",
        "price",
        "attendance_days",
        "status",
    )

    list_filter = (
        "plan_type",
        "status",
    )

    search_fields = ("name",)