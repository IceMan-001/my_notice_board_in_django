# from django.db import models
#
#
# # Create your models here.
# class Post(models.Model):  # наследуется от базового импортированного класса
#     # имя поля = названию столбца в таблице с настройками поля
#     # CharField --> строковое значение, max_length --> максимальная длина поля 50 байт
#     # по умолчанию NOT NULL = False
#     # verbose_name --> человеко читаемое имя
#     author = models.CharField(max_length=50, verbose_name='Автор')
#     title = models.CharField(max_length=200, verbose_name='Заголовок')
#     # TextField --> не обязательно указывать длину
#     text = models.TextField(verbose_name='Текст объявления')
#
#     # Настроечный класс
#     class Meta:
#         # Указываем название таблицы для админки единственное и множественное число
#         verbose_name = 'Объявление'
#         verbose_name_plural = 'Объявления'

#
# # после изменений нужно провести миграции
# # и регистрации в файле admin.py

from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    # поля таблицы
    author = models.CharField(max_length=50, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=500, verbose_name='Текст объявления')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано',
                                      editable=False)  # Параметр 'editable' отключает возможность для редактирования
    url_adders = models.CharField(max_length=150, verbose_name='Ссылка на сайт')
    image = models.ImageField(upload_to='posts/', null=True, verbose_name='Изображение')

    class Meta:  # Настроечный класс
        # Имя таблицы в единственном числе
        verbose_name = 'Объявление'
        # Имя таблицы
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
