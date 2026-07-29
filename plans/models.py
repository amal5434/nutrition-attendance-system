from django.db import models


class Plan(models.Model):

    PLAN_TYPES = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Custom", "Custom"),
    ]

    STATUS = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    name = models.CharField(max_length=100)

    plan_type = models.CharField(
        max_length=20,
        choices=PLAN_TYPES
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    attendance_days = models.PositiveIntegerField()

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name