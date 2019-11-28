from django.db import models
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField


class Author(models.Model):
	author_name = models.CharField('ФИО автора', max_length = 50)
	avatar = models.ImageField('Изображение', null = True, blank = True, upload_to = 'img/')

	def __str__(self):
		return self.author_name


	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'


class Genre(MPTTModel):

	class Meta:
		verbose_name = 'Рубрика'
		verbose_name_plural = 'Рубрики'

	name = models.CharField('Рубрика', max_length=50)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name = 'Входит в')
	class MPTTMeta:
		order_insertion_by = ['name']
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name



class Article(models.Model):
	article_title = models.CharField('Заголовок', max_length = 100)
	article_announcement = models.CharField('Анонс', max_length = 250)
	article_text = models.TextField('Текст')
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	genre = TreeManyToManyField(Genre, null=True, help_text="Выберите рубрику новости")

	def __str__(self):
		return self.article_title


	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

	