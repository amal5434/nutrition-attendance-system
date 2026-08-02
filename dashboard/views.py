import json
from datetime import timedelta
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from customers.models import Customer
from billing.models import CustomerPlan, Invoice
from attendance.models import Attendance


@login_required
def dashboard_home(request):
    # Only Admin (superuser) users can view the dashboard & revenue metrics
    if not request.user.is_superuser:
        messages.warning(request, "Access Denied: Staff members do not have access to financial revenue metrics.")
        return redirect('home')

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

    # Calculate last 7 consecutive days of revenue
    chart_labels = []
    chart_data = []

    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        day_revenue = Invoice.objects.filter(
            created_at__date=day
        ).aggregate(total=Sum('payment_received'))['total'] or 0

        chart_labels.append(day.strftime('%d %b'))
        chart_data.append(float(day_revenue))

    return render(request, 'dashboard/home.html', {
        'total_customers': total_customers,
        'active_plans': active_plans,
        'today_attendance': today_attendance,
        'today_revenue': today_revenue,
        'chart_labels_json': json.dumps(chart_labels),
        'chart_data_json': json.dumps(chart_data),
    })