from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import empdata
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from .models import Service
from .forms import ServiceForm
from django.contrib.admin.views.decorators import staff_member_required

@login_required(login_url='login')
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        address = request.POST.get('address', '').strip()
        contactno = request.POST.get('contactno', '').strip()
        location = request.POST.get('location', '').strip()
        if not all([name, email, password, address, contactno, location]):
            messages.error(request, "All fields are required!")
            return redirect('signup')
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Enter a valid email address.")
            return redirect('signup')
        if not contactno.isdigit() or len(contactno) != 10:
            messages.error(request, "Invalid phone number. It must be exactly 10 digits.")
            return redirect('signup')
        if User.objects.filter(username=name).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Username or Email already exists!")
            return redirect('signup')
        user = User.objects.create_user(username=name, email=email, password=password)
        empdata.objects.create(
            name=name,
            email=email,
            password=password,
            address=address,
            contact_no=contactno,
            location=location)
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')
    return render(request, 'signup.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both fields are required!")
            return redirect('signup')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'signup.html')
        
def logoutpage(request):
    logout(request)
    return redirect('login')

def frontpage(request):
    return render(request,'frontpage.html')

def header(request):
    return render(request,'header.html')

def content(request):
    return render(request,'content.html')

def homepage(request):
    return render(request,'homepage.html')

def profile(request):
    return render(request,'profile.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

@login_required
@staff_member_required 
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})

def plumber(request):
    selected_location = request.GET.get('location', '')
    services = Service.objects.filter(service_type='PLUMBER')
    if selected_location:
        services = services.filter(address__icontains=selected_location)
    locations = Service.objects.filter(service_type='PLUMBER') \
                               .values_list('address', flat=True).distinct()
    return render(request, 'plumber.html', {
        'services': services,
        'locations': locations,
    })

def carpenter(request):
    selected_location = request.GET.get('location', '')
    services = Service.objects.filter(service_type='CARPENTER')
    if selected_location:
        services = services.filter(address__icontains=selected_location)
    locations = Service.objects.filter(service_type='CARPENTER') \
                               .values_list('address', flat=True).distinct()
    return render(request, 'carpenter.html', {
        'services': services,
        'locations': locations,
    })

def electrician(request):
    selected_location = request.GET.get('location', '')
    services = Service.objects.filter(service_type='ELECTRICIAN')
    if selected_location:
        services = services.filter(address__icontains=selected_location)
    locations = Service.objects.filter(service_type='ELECTRICIAN') \
                               .values_list('address', flat=True).distinct()
    return render(request, 'electrician.html', {
        'services': services,
        'locations': locations,
    })

def tvtech(request):
    selected_location = request.GET.get('location', '')
    services = Service.objects.filter(service_type='TV TECH')
    if selected_location:
        services = services.filter(address__icontains=selected_location)
    locations = Service.objects.filter(service_type='TV TECH') \
                               .values_list('address', flat=True).distinct()
    return render(request, 'tvtech.html', {
        'services': services,
        'locations': locations,
    })

def plum(request):
    return render(request,'plum.html')

def elect(request):
    return render(request,'elect.html')

def tvtec(request):
    return render(request,'tv.html')

def carp(request):
    return render(request, 'carp.html')
