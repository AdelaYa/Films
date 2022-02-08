from django.views.generic import ListView, DetailView
from . models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(ListView):
    model = Post
    template_name = 'index.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    login_url = 'login'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    login_url = 'login'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'post_text']
    template_name = 'post_edit.html'
    login_url = 'login'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')
    login_url = 'login'