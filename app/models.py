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
        db_table = "Comments"
        ordering = ["-date"]
        verbose_name = "Комментарии к статье блога"
        verbose_name_plural = "Комментарии к статьям блога"

admin.site.register(Comment)

class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название статуса")
    
    def get_absolute_url(self):
        return reverse("statuses", args=[str(self.id)])
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Statuses"# имя таблицы для модели
        verbose_name = "Статус заказа" 
        verbose_name_plural = "Статусы заказа" 
        
admin.site.register(Status)

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Покупатель")
    date = models.DateTimeField(default= datetime.now(), db_index=True, verbose_name= "Дата заказа")
    order_status = models.ForeignKey(Status, on_delete = models.CASCADE, verbose_name = "Статус заказа")
    total_price = models.FloatField(verbose_name = "Итоговая сумма заказа")
    
    class Meta:
        db_table = "Orderes"# имя таблицы для модели
        ordering = ["date"]
        verbose_name = "Заказ" 
        verbose_name_plural = "Заказы" 
        
admin.site.register(Order)
    
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название категории товаров")
    
    def get_absolute_url(self):
        return reverse("сategories", args=[str(self.id)])
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Categories"# имя таблицы для модели
        verbose_name = "Категория товара" 
        verbose_name_plural = "Категории товаров" 

admin.site.register(Category)

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Краткое описание")
    price = models.FloatField(verbose_name = "Цена")
    image = models.FileField(default='temp.jpg', verbose_name = "Путь к картинке")
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = "Категория товара")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Products"# имя таблицы для модели
        verbose_name = "Товар" 
        verbose_name_plural = "Список товаров" 
        
admin.site.register(Product)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete = models.CASCADE, verbose_name = "Заказ")
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = "Товар")
    price_quantity = models.FloatField(verbose_name = "Цена за количество")
    quantity = models.IntegerField(verbose_name = "Количество")
    
    class Meta:
        db_table = "OrderItems" # имя таблицы для модели
        ordering = ["order_id"] # Сортировка по Id заказа
        verbose_name = "Товар в заказе" 
        verbose_name_plural = "Товары в заказе" 
        
admin.site.register(OrderItem)