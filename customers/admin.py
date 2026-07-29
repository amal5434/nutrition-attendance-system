from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "customer_code",
        "first_name",
        "phone",
        "status",
    )

    search_fields = (
        "customer_code",
        "first_name",
        "phone",
    )