from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan
from .forms import PlanForm
from django.http import JsonResponse


def plan_list(request):

    plans = Plan.objects.all().order_by("name")

    return render(
        request,
        "plans/plan_list.html",
        {"plans": plans}
    )


def plan_add(request):

    if request.method == "POST":

        form = PlanForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("plan_list")

    else:
        form = PlanForm()

    return render(
        request,
        "plans/plan_form.html",
        {"form": form}
    )

def plan_price(request, plan_id):

    plan = Plan.objects.get(id=plan_id)

    return JsonResponse({
        "price": float(plan.price),
        "days": plan.attendance_days,
    })
def plan_edit(request, plan_id):

    plan = get_object_or_404(Plan, id=plan_id)

    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)

        if form.is_valid():
            form.save()
            return redirect("plan_list")
    else:
        form = PlanForm(instance=plan)

    return render(request, "plans/plan_form.html", {
        "form": form,
        "title": "Edit Plan"
    })


def plan_toggle_status(request, plan_id):

    plan = get_object_or_404(Plan, id=plan_id)

    if plan.status == "Active":
        plan.status = "Inactive"
    else:
        plan.status = "Active"

    plan.save()

    return redirect("plan_list")


def plan_delete(request, plan_id):

    plan = get_object_or_404(Plan, id=plan_id)

    plan.delete()

    return redirect("plan_list")