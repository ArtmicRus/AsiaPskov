"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date= "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default= datetime.now(), db_index=True, verbose_name="Опубликована")
    
    #Методы класса:
    
    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])
    def __str__(self):
        return self.title
    
    #Метаданные вложенный класс который задаёт дополнительные параметры модели
    class Meta:
        db_table = "Posts"# имя таблицы для модели
        ordering = ["-posted"] # Порядок сортировки данных в модели (- это убывание)
        verbose_name = "статья блога" #Имя которое будет отображаться в администратимном разделе (для одной статьи)
        verbose_name_plural = "статья блога" #Для всех статей

admin.site.register(Blog)
