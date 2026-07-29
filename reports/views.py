import pandas as pd

from django.shortcuts import render
from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import letter

from billing.models import Invoice
from attendance.models import Attendance


def report_home(request):
    return render(request, 'reports/report_home.html')


# ---------------- EXCEL ----------------

def invoice_excel(request):

    invoices = Invoice.objects.select_related('customer', 'plan')

    data = []

    for inv in invoices:
        data.append({
            'Invoice No': inv.invoice_no,
            'Customer': inv.customer.first_name,
            'Plan': inv.plan.name,
            'Amount': float(inv.final_amount),
            'Paid': float(inv.payment_received),
            'Balance': float(inv.balance),
            'Date': inv.created_at.strftime('%d-%m-%Y'),
        })

    df = pd.DataFrame(data)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename=invoices.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Invoices')

    return response


# ---------------- PDF ----------------

def invoice_pdf(request):

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=invoices.pdf'

    doc = SimpleDocTemplate(response, pagesize=letter)

    data = [['Invoice', 'Customer', 'Plan', 'Amount', 'Paid', 'Balance']]

    for inv in Invoice.objects.select_related('customer', 'plan'):
        data.append([
            inv.invoice_no,
            inv.customer.first_name,
            inv.plan.name,
            str(inv.final_amount),
            str(inv.payment_received),
            str(inv.balance),
        ])

    table = Table(data)

    doc.build([table])

    return response


# ---------------- ATTENDANCE EXCEL ----------------

def attendance_excel(request):

    records = Attendance.objects.select_related('customer', 'customer_plan')

    data = []

    for a in records:
        data.append({
            'Customer': a.customer.first_name,
            'Plan': a.customer_plan.plan.name,
            'Date': a.attendance_date.strftime('%d-%m-%Y'),
            'Time': a.check_in_time.strftime('%H:%M'),
            'Remaining Days': a.customer_plan.remaining_days,
        })

    df = pd.DataFrame(data)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename=attendance.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Attendance')

    return response


# ---------------- ATTENDANCE PDF ----------------

def attendance_pdf(request):

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename=attendance.pdf'

    doc = SimpleDocTemplate(response, pagesize=letter)

    data = [['Customer', 'Plan', 'Date', 'Time', 'Remaining']]

    for a in Attendance.objects.select_related('customer', 'customer_plan'):
        data.append([
            a.customer.first_name,
            a.customer_plan.plan.name,
            str(a.attendance_date),
            str(a.check_in_time),
            str(a.customer_plan.remaining_days),
        ])

    table = Table(data)

    doc.build([table])

    return response