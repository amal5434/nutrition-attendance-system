from decimal import Decimal
from datetime import date, timedelta

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import InvoiceForm
from .models import Invoice, CustomerPlan


@login_required
def invoice_create(request):

    if request.method == "POST":

        form = InvoiceForm(request.POST)

        if form.is_valid():

            invoice = form.save(commit=False)

            plan = invoice.plan

            invoice.package_price = plan.price

            # -------- DISCOUNT CALCULATION --------
            if invoice.discount_type == "Fixed":

                final_amount = plan.price - invoice.discount_value

            elif invoice.discount_type == "Percentage":

                final_amount = plan.price - (
                    plan.price * invoice.discount_value / Decimal("100")
                )

            else:
                final_amount = plan.price

            invoice.final_amount = final_amount

            invoice.balance = final_amount - invoice.payment_received

            invoice.invoice_no = f"INV{Invoice.objects.count()+1:05d}"

            invoice.save()

            # -------- CREATE CUSTOMER PLAN --------
            CustomerPlan.objects.create(
                customer=invoice.customer,
                plan=plan,
                purchased_days=plan.attendance_days,
                remaining_days=plan.attendance_days,
                start_date=date.today(),
                expiry_date=date.today() + timedelta(days=30),
                final_amount=invoice.final_amount,
                paid_amount=invoice.payment_received,
                balance_amount=invoice.balance,
            )

            return redirect("invoice_create")

    else:
        form = InvoiceForm()

    return render(request, "billing/invoice_form.html", {"form": form})
@login_required
def invoice_list(request):

    invoices = Invoice.objects.select_related(
        'customer',
        'plan'
    ).order_by('-created_at')

    return render(request, 'billing/invoice_list.html', {
        'invoices': invoices
    })