from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count

from django.db.models import Q
from customers.models import Customer
from billing.models import CustomerPlan
from .models import Attendance


def attendance_home(request):

    query = request.GET.get('q', '').strip()

    customer = None
    active_plan = None

    if query:

        customer = Customer.objects.filter(
            Q(customer_code__icontains=query) |
            Q(phone__icontains=query)
        ).first()

        if customer:
            active_plan = CustomerPlan.objects.filter(
                customer=customer,
                remaining_days__gt=0
            ).first()

    return render(request, 'attendance/attendance_home.html', {
        'query': query,
        'customer': customer,
        'active_plan': active_plan,
    })

def attendance_list(request):

    attendances = Attendance.objects.select_related(
        'customer',
        'customer_plan'
    )

    return render(request, 'attendance/attendance_list.html', {
        'attendances': attendances
    })


def check_in(request, customer_id):

    customer = get_object_or_404(Customer, id=customer_id)

    # Get active plan with remaining days
    customer_plan = CustomerPlan.objects.filter(
        customer=customer,
        remaining_days__gt=0
    ).first()

    if not customer_plan:
        messages.error(request, 'No active plan available for this customer.')
        return redirect('customer_list')

    # Prevent duplicate attendance on same day
    today = timezone.now().date()

    already_marked = Attendance.objects.filter(
        customer=customer,
        attendance_date=today
    ).exists()

    if already_marked:
        messages.warning(request, 'Attendance already marked for today.')
        return redirect('attendance_list')

    # Create attendance
    Attendance.objects.create(
        customer=customer,
        customer_plan=customer_plan
    )

    # Deduct remaining day
    customer_plan.remaining_days -= 1
    customer_plan.save()

    messages.success(
        request,
        f'Attendance marked successfully. Remaining days: {customer_plan.remaining_days}'
    )

    return redirect('home')
def attendance_report(request):

    report = Attendance.objects.values(
        'attendance_date'
    ).annotate(
        total=Count('id')
    ).order_by('-attendance_date')

    return render(request, 'attendance/attendance_report.html', {
        'report': report
    })