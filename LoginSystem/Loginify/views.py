from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .models import UserDetails
from django.contrib import messages # type: ignore

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if UserDetails.objects.filter(email = email).exists():
            return render(request, 'Loginify/signup.html', {'error' : 'Email already registered.'})
        
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    
    return render(request, 'Loginify/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(email=email, password=password)
            return render(request, 'Loginify/success.html', {'username': user.username})
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'Loginify/login.html')


def success_view(request):
    return render(request, 'Loginify/success.html')