from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm

# Create your views here.
class SignUp(CreateView):
    form_class = SignUpForm
    # Redirect to login page post successful SignUp
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

