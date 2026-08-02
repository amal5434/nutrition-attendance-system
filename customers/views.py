from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm

@login_required
def customer_list(request):
    customers = Customer.objects.all().order_by("customer_code")
    return render(request, "customers/customer_list.html", {
        "customers": customers
    })


@login_required
def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("customer_list")

    else:
        form = CustomerForm()

    return render(request, "customers/customer_form.html", {
        "form": form
    })