from django.db import models
from customers.models import Customer
from billing.models import CustomerPlan


class Attendance(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    customer_plan = models.ForeignKey(CustomerPlan, on_delete=models.CASCADE)

    attendance_date = models.DateField(auto_now_add=True)

    check_in_time = models.TimeField(auto_now_add=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-attendance_date', '-check_in_time']

    def __str__(self):
        return f"{self.customer} - {self.attendance_date}"