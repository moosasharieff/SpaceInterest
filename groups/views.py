from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from models import Group
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    """ This class method creates group """
    fields = ['name', 'description']
    model = Group

class SingleGroup(generic.DetailView):
    """ This class creates detail view for a single group """
    model = Group

class ListGroup(generic.ListView):
    """ This class lists all the created groups """
    model = Group
