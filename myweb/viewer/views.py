from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())


def about_me(request):
    template = loader.get_template("about_me.html")
    return HttpResponse(template.render())


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "base.html"


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    template_name = "post_form.html"
    form_class = PostForm
    success_url = reverse_lazy("index")


class PostDeleteView(DeleteView):
    template_name = "post_delete.html"
    model = Post
    success_url = reverse_lazy("index")


class PostUpdateView(UpdateView):
    template_name = "post_form.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("index")