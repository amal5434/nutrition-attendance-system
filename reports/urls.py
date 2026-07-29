from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_home, name='report_home'),

    path('invoices/excel/', views.invoice_excel, name='invoice_excel'),
    path('invoices/pdf/', views.invoice_pdf, name='invoice_pdf'),

    path('attendance/excel/', views.attendance_excel, name='attendance_excel'),
    path('attendance/pdf/', views.attendance_pdf, name='attendance_pdf'),
]