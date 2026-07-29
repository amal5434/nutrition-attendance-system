from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum

from customers.models import Customer
from billing.models import CustomerPlan, Invoice
from attendance.models import Attendance


def dashboard_home(request):

    today = timezone.now().date()

    total_customers = Customer.objects.count()

    active_plans = CustomerPlan.objects.filter(
        remaining_days__gt=0
    ).count()

    today_attendance = Attendance.objects.filter(
        attendance_date=today
    ).count()

    today_revenue = Invoice.objects.filter(
        created_at__date=today
    ).aggregate(
        total=Sum('payment_received')
    )['total'] or 0

    # Last 7 invoices for chart
    invoices = Invoice.objects.order_by('-created_at')[:7]

    chart_labels = [
        invoice.created_at.strftime('%d %b')
        for invoice in reversed(invoices)
    ]

    chart_data = [
        float(invoice.payment_received)
        for invoice in reversed(invoices)
    ]

    return render(request, 'dashboard/home.html', {
        'total_customers': total_customers,
        'active_plans': active_plans,
        'today_attendance': today_attendance,
        'today_revenue': today_revenue,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    })