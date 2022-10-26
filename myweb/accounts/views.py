from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm
# Create your views here.


class SignUpView(CreateView):
    template_name = "forms.html"
    form_class = SignUpForm
