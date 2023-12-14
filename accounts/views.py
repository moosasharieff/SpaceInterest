from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm

# Create your views here.
class SignUp(CreateView):
    form_class = SignUpForm
    # Redirect to login page post successful SignUp
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def logoutUser(request):
    """ Handles logout functionality for the application """
    logout(request)
    return redirect('home')