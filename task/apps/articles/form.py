from django import forms

from .models import Article, Author, Genre

class NewArticle(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('article_title', 'article_announcement', 'article_text', 'author', 'genre')

class NewAuthor(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('author_name', 'avatar')

class NewGenre(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ('name', 'parent')