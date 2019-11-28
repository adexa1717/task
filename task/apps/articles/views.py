from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import NewArticle, NewAuthor, NewGenre

from .models import Author, Article, Genre

def index(request):
	
	search_query = request.GET.get('search','')

	if search_query:
		articles_list = Article.objects.filter(article_title__icontains = search_query)
	else:
		articles_list = Article.objects.order_by('-id')
	
	return render(request, 'articles/list.html', {'articles_list':articles_list})



def main(request):
	return render(request, 'articles/main.html')

def detail(request, article_id):
	try:
		a = Article.objects.get( id = article_id)
	except:
		raise Http404("Нвость отсутствует!")

	return render(request, 'articles/detail.html', {'article':a, 'genres': a.genre.all()})

def author_detail(request, author_id):
	try:
		at = Author.objects.get( id = author_id)
	except:
		raise Http404("Автора нет!")

	return render(request, 'articles/author_detail.html', {'author':at, 'articles': Article.objects.filter(author_id = author_id)})

def show_genres(request):

	search_query = request.GET.get('search','')

	if search_query:
		genre_list = Genre.objects.filter(name__icontains = search_query)
	else:
		genre_list = Genre.objects.all()

	return render(request, "articles/genre.html", {'genres': genre_list})

def genre_detail(request, genre_id):
	try:
		gi = Genre.objects.get( id = genre_id)
	except:
		raise Http404("Рубрика жок!")

	return render(request, 'articles/genre_detail.html', {'node':gi, 'articles': Article.objects.filter(genre = gi)})

def authors(request):
	authors_list = Author.objects.order_by('-id')[:5]
	return render(request, 'articles/authors.html', {'authors_list':authors_list})

def author_new(request):
	if request.method == "POST":
		form = NewAuthor(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('articles:author_detail', author_id = post.id)
	else:
		form = NewAuthor()
	return render(request, 'articles/author_new.html', {'form': form})

def author_edit(request, author_id):
    try:
    	post = Author.objects.get( id = author_id)
    except:
    	raise Http404("Автора нет!")
    if request.method == "POST":
        form = NewAuthor(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('articles:author_detail', author_id=post.id)
    else:
        form = NewAuthor(instance=post)
    return render(request, 'articles/author_edit.html', {'form': form})

def article_new(request):
	if request.method == "POST":
		form = NewArticle(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('articles:detail', article_id = post.id)
	else:
		form = NewArticle()
	return render(request, 'articles/article_new.html', {'form': form})

def article_edit(request, article_id):
    try:
    	post = Article.objects.get( id = article_id)
    except:
    	raise Http404("Нвость отсутствует!")
    if request.method == "POST":
        form = NewArticle(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('articles:detail', article_id=post.id)
    else:
        form = NewArticle(instance=post)
    return render(request, 'articles/article_edit.html', {'form': form})

def genre_new(request):
	if request.method == "POST":
		form = NewGenre(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('articles:genre_detail', genre_id = post.id)
	else:
		form = NewGenre()
	return render(request, 'articles/genre_new.html', {'form': form})

def genre_edit(request, genre_id):
    try:
    	post = Genre.objects.get( id = genre_id)
    except:
    	raise Http404("Рубрика жок!")
    if request.method == "POST":
        form = NewGenre(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('articles:genre_detail', genre_id=post.id)
    else:
        form = NewGenre(instance=post)
    return render(request, 'articles/genre_edit.html', {'form': form})