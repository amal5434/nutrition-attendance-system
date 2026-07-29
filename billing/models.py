from django.db import models
from customers.models import Customer
from plans.models import Plan


class CustomerPlan(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    purchased_days = models.PositiveIntegerField()

    remaining_days = models.PositiveIntegerField()

    start_date = models.DateField()

    expiry_date = models.DateField()

    final_amount = models.DecimalField(max_digits=10, decimal_places=2)

    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.plan}"


class Invoice(models.Model):

    DISCOUNT_TYPES = [
        ("Fixed", "Fixed"),
        ("Percentage", "Percentage"),
    ]

    invoice_no = models.CharField(max_length=30, unique=True)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    package_price = models.DecimalField(max_digits=10, decimal_places=2)

    discount_type = models.CharField(
        max_length=20,
        choices=DISCOUNT_TYPES,
        blank=True
    )

    discount_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    final_amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_received = models.DecimalField(max_digits=10, decimal_places=2)

    balance = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_no
    