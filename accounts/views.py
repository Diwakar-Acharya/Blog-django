from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # After signup, go to login page
    template_name = 'registration/signup.html'


# accounts/views.py
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = UserLoginForm # <--- This connects the styles!