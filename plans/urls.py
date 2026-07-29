from django.urls import path
from . import views

urlpatterns = [
    path("", views.plan_list, name="plan_list"),

    path("add/", views.plan_add, name="plan_add"),

    path("edit/<int:plan_id>/", views.plan_edit, name="plan_edit"),

    path("toggle/<int:plan_id>/", views.plan_toggle_status, name="plan_toggle_status"),

    path("delete/<int:plan_id>/", views.plan_delete, name="plan_delete"),

    path("price/<int:plan_id>/", views.plan_price, name="plan_price"),
]