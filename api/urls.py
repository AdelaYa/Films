from django.urls import path
from .views import FilmApiView, FilmApiDetail

urlpatterns = [
    path('', FilmApiView.as_view()),
    path('<int:pk>/', FilmApiDetail.as_view()),
]