from django.db import models


class Customer(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    customer_code = models.CharField(max_length=20, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()

    joining_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_code} - {self.first_name} {self.last_name}"