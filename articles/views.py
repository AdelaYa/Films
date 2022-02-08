from django.views.generic import ListView, DetailView
from . import models
from django.views.generic.edit import  UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticlesView(ListView):
    model = models.Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin,  DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title', 'content']
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'content']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleCommentView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = 'article_comment.html'
    fields = ['comment', 'author']
    login_url = 'login'





