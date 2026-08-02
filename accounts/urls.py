from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_portal, name='login'),
    path('admin/', views.admin_login, name='admin_login'),
    path('staff/', views.staff_login, name='staff_login'),
    path('logout/', views.logout_view, name='logout'),
]
