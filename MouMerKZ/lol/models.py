from django.db import models
from django.urls import reverse


class Lol(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описания")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создание")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменение")
    is_published = models.BooleanField(default=True, verbose_name="Публикован")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class FlashGames(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    file = models.FileField(upload_to='games/', verbose_name="Загружить файл(SWF)")  # Путь для загрузки файлов флэш-игр
    post = models.ForeignKey(Lol, on_delete=models.CASCADE, related_name='flash_games')  # Связь с моделью Post
    width = models.PositiveIntegerField(default=640)
    height = models.PositiveIntegerField(default=480)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Флэш игра'
        verbose_name_plural = 'Флэш игры'
