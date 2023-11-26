"""
Definition of models.
"""

from email.mime import image
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date= "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default= datetime.now(), db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default='temp.jpg', verbose_name = "Путь к картинке")
    
    # Методы класса:
    
    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])
    def __str__(self):
        return self.title
    
    # Метаданные вложенный класс который задаёт дополнительные параметры модели
    class Meta:
        db_table = "Posts"# имя таблицы для модели
        ordering = ["-posted"] # Порядок сортировки данных в модели (- это убывание)
        verbose_name = "статья блога" #Имя которое будет отображаться в администратимном разделе (для одной статьи)
        verbose_name_plural = "статьи блога" #Для всех статей

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default= datetime.now(), db_index=True, verbose_name= "Дата комментария")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор комментария")
    post = models.ForeignKey(Blog,on_delete=models.CASCADE, verbose_name= "Статья комментария")
    # Методы класса:
    def __str__(self):
        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)
    # Метаданные вложенный класс который задает дополнительные параметры модели:
    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = "Комментарии к статье блога"
        verbose_name_plural = "Комментарии к статьям блога"

admin.site.register(Comment)

class OrderStatus(models.Model):
    status_name = models.CharField(max_length=30, unique_for_date= "posted", verbose_name="Название статуса")
    
    def __str__(self):
        return self.status_name

    class Meta:
        db_table = "OrderStatuses"# имя таблицы для модели
        verbose_name = "Статус заказа" 
        verbose_name_plural = "Статусы заказа" 
        
admin.site.register(OrderStatus)

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Покупатель")
    date = models.DateTimeField(default= datetime.now(), db_index=True, verbose_name= "Дата заказа")
    order_status = models.ForeignKey(OrderStatus, on_delete = models.CASCADE, verbose_name = "Статус заказа")
    total_price = models.FloatField(verbose_name = "Итоговая сумма заказа")
    
    class Meta:
        db_table = "OrderStatuses"# имя таблицы для модели
        ordering = ["date"]
        verbose_name = "Статус заказа" 
        verbose_name_plural = "Статусы заказа" 
        
admin.site.register(Order)


