from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from .models import Profile, User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.


class SignUpView(CreateView):
    template_name = "forms.html"
    form_class = SignUpForm
    success_url = reverse_lazy("index")


class CustomLoginView(LoginView):
    template_name = "forms.html"


class UserListView(ListView):
    template_name = "users.html"
    queryset = Profile.objects.all()


class BiographyView(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    context_object_name = "profile"




