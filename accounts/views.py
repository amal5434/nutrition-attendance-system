from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_portal(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('dashboard_home')
        return redirect('home')
    
    role = request.GET.get('role', 'admin')
    return render(request, 'accounts/login.html', {'role': role})

def admin_login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username', '').strip()
        p_word = request.POST.get('password', '').strip()
        
        user = authenticate(request, username=u_name, password=p_word)
        if user is not None:
            if user.is_superuser or user.is_staff:
                login(request, user)
                messages.success(request, f"Welcome Admin, {user.first_name or user.username}!")
                return redirect('dashboard_home')
            else:
                messages.error(request, "Access denied: Account does not have Admin credentials.")
                return redirect('/login/?role=admin')
        else:
            messages.error(request, "Invalid Admin username or password.")
            return redirect('/login/?role=admin')
            
    return redirect('/login/?role=admin')

def staff_login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username', '').strip()
        p_word = request.POST.get('password', '').strip()
        
        user = authenticate(request, username=u_name, password=p_word)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome Staff, {user.first_name or user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Staff username or password.")
            return redirect('/login/?role=staff')
            
    return redirect('/login/?role=staff')

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')
