from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect("/customers/")

urlpatterns = [
    path('', include('dashboard.urls')),
    path("admin/", admin.site.urls),
    path("customers/", include("customers.urls")),
    path("plans/", include("plans.urls")),
    path("billing/", include("billing.urls")),
    path('attendance/', include('attendance.urls')),
    path('reports/', include('reports.urls')),
]