from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm
from django.shortcuts import render, redirect, get_object_or_404


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


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.first_name = request.POST.get("first_name")
        customer.last_name = request.POST.get("last_name")
        customer.phone = request.POST.get("phone")
        customer.age = request.POST.get("age")
        customer.gender = request.POST.get("gender")

        customer.save()

        return redirect("customer_list")

    return render(
        request,
        "customers/customer_edit.html",
        {"customer": customer}
    )


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")

    return render(
        request,
        "customers/customer_confirm_delete.html",
        {"customer": customer}
    )