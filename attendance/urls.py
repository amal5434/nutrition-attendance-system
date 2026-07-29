from django.urls import path
from . import views

urlpatterns = [

    path('', views.attendance_list, name='attendance_list'),

    path('report/', views.attendance_report, name='attendance_report'),

    path('check-in/<int:customer_id>/', views.check_in, name='check_in'),
]