from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='article_list'),
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/comment/', views.ArticleCommentView.as_view(), name='article_comment'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]