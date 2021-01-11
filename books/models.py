from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    city = models.CharField(max_length=60, verbose_name='Город')
    state_province = models.CharField(max_length=30, verbose_name='Область')
    country = models.CharField(max_length=50, verbose_name='Страна')
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    email = models.EmailField(blank=True)  # необязательное поле

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    authors = models.ManyToManyField(Author, verbose_name='Авторы')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='Издатели')
    publication_date = models.DateField(verbose_name='Дата издания')

    def __str__(self):
        return self.title
