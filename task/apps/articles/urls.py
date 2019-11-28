from django.http import Http404, HttpResponseRedirect
from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
	path('', views.main, name = 'main'),
	path('articles/', views.index, name = 'index'),
	path('authors/', views.authors, name = 'authors'),
	path('articles/<int:article_id>/', views.detail, name = 'detail'),
	path('author/<int:author_id>/', views.author_detail, name = 'author_detail'),
	path('genre/', views.show_genres, name = 'show_genres'),
	path('genre_detail/<int:genre_id>/', views.genre_detail, name = 'genre_detail'),
	path('articles/article_new/', views.article_new, name='article_new'),
	path('articles/<int:article_id>/article_edit/', views.article_edit, name='article_edit'),
	path('articles/author_new/', views.author_new, name='author_new'),
	path('author/<int:author_id>/author_edit/', views.author_edit, name='author_edit'),
	path('articles/genre_new/', views.genre_new, name='genre_new'),
	path('genre_detail/<int:genre_id>/genre_edit/', views.genre_edit, name='genre_edit'),
]