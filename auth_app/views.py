from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Registration (Sign-Up) View
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        phone_code = request.POST.get('phone_code')
        description = request.POST.get('description')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'sign_up.html',{'error': 'Username already exists. Please choose a different username.'})
            else:
                # Create a new user
                user = User.objects.create_user(username=username, password=password1)
                user.first_name=first_name
                user.last_name=last_name
                user.email=email
                user.save()
                messages.success(request, 'Account created successfully! You can now log in.')
                custom_user=CustomUser.objects.create(user=user,company_name=company_name,phone_number=phone_code)
                custom_user.description=description
                custom_user.country=country
                custom_user.save()
                return redirect(f"{reverse('login')}?message=Account+created+successfully!+You+can+now+log+in.")
        else:
            return render(request, 'sign_up.html',{'error': 'Passwords do not match. Please try again.'})
    return render(request, 'sign_up.html')

# Login View
def login(request):
    message = request.GET.get('message', None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_authenticated and user.is_superuser:
                return redirect('user_list')
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')  # Redirect to the home page after successful login
        else:
            return render(request, 'login.html',{'error':'Invalid username or password.'})

    return render(request, 'login.html',{'message':message})

# Logout View
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')  # Redirect to the home page after logout


def home(request):
    return render(request, 'index.html')

def digital_distribution(request):
    return render(request, 'digital_distribution.html')


def music_distribute(request):
    return render(request, 'music_distribute.html')

def music_publishing(request):
    return render(request, 'music_publishing.html')

def rights_management(request):
    return render(request, 'rights_management.html')

def sell(request):
    return render(request, 'sell.html')

def service(request):
    return render(request, 'service.html')

def stores(request):
    return render(request, 'stores.html')

def support(request):
    return render(request, 'support.html')

def youtube_monetization(request):
    return render(request, 'youtube_monetization.html')


@login_required
def user_list(request):
    if not request.user.is_superuser:
        return redirect('home')
    users = CustomUser.objects.select_related('user').all()

    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(user__username__icontains=search_query) | \
                users.filter(user__email__icontains=search_query) | \
                users.filter(company_name__icontains=search_query)

    # Pagination
    paginator = Paginator(users, 10)  # Show 10 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'user_list.html', context)