from django.contrib import admin
from django.urls import path, include
from attendance import views as attendance_views

urlpatterns = [

    # MAIN PAGE
    path('', attendance_views.attendance_home, name='home'),

    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('plans/', include('plans.urls')),
    path('billing/', include('billing.urls')),
    path('attendance/', include('attendance.urls')),
    path('reports/', include('reports.urls')),
    path('dashboard/', include('dashboard.urls')),
]