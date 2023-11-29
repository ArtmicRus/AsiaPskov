"""
Definition of views.
"""
from asyncio.windows_events import NULL
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpRequest
from django.urls import reverse
from .forms import BlogForm, FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from django.db import models
from .models import Blog, OrderItem

from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария

from .models import Category
from .models import Product
from .models import Order
from .models import Status

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведение о нас',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Ссылки',
            'message':'Ссылки на нас и наши ресурсы',
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария
            

    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы добавления комментария в шаблон веб-страницы
            
            'year':datetime.now().year,
        }
    )

def newpost(request):
    """Renders the newpost page."""
    assert isinstance(request,HttpRequest)
    
    if request.method == "POST":
        blogform = BlogForm(request.POST,request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()
            
            return redirect('blog')
    else:
        blogform = BlogForm()
        
    return render(
        request,
        'app/newpost.html',
        {
            'blogform':blogform,
            'title': 'Добавить статью блога',
            
            'year':datetime.now().year,
        }
    )

def videopost(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            
            'year':datetime.now().year,
        }
    )

def feedback(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1':'Мужчина','2':'Женщина'}
    delivery = {'1':'1-3','2':'4-6','3':'7-9','4':'Больше 9 раз в месяц'}
    if request.method=='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['gender'] = gender [form.cleaned_data['gender']]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['delivery']= delivery [form.cleaned_data['delivery']]
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = FeedbackForm()    
    return render(
        request,
        'app/feedback.html',
        {
            'form':form,
            'data':data
        }
    )

def registration(request):
    """Renders the registration page."""
    
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
        
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )

def catalog(request, cat_id = 0):
    """Renders the category page."""
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all() # запрос на выбор всех статей блога из модели
    products = Product.objects.filter(category_id = cat_id)
    
    if len(products) == 0:
        products = Product.objects.all()
        
    return render(
        request,
        'app/catalog.html',
        {
            'title':'Меню',
            'categories':categories,
            'cat_selected':cat_id,
            'products':products,
            'year':datetime.now().year,
        }
    )

def cart(request):
    """Renders the cart page."""
    assert isinstance(request, HttpRequest)
    current_order = Order.objects.filter(user=request.user, order_status_id=1).first()
    
    if current_order == None:
        items = None
    else:
        items = OrderItem.objects.filter(order=current_order)
        
    return render(
        request,
        'app/cart.html',
        {
            'title':'Корзина',
            'order': current_order,
            'items': items,  
            'year':datetime.now().year,
        }
    )

def add_to_cart(request):

    current_product = Product.objects.filter(id = request.GET.get('product')).first()
    current_order, order_status_id = Order.objects.get_or_create(user=request.user, order_status_id=1)
    if order_status_id:
        current_order.save()
    CartItem, order_status_id = OrderItem.objects.get_or_create(order=current_order, product=current_product)
    CartItem.quantity += 1
    CartItem.price_quantity = CartItem.product.price * CartItem.quantity
    CartItem.save()
    CartItem_list = OrderItem.objects.filter(order=current_order)
    current_order.total_price = 0
    for item in CartItem_list:
        current_order.total_price += item.price_quantity

    current_order.save()
    assert isinstance(request, HttpRequest)
    return redirect(reverse('catalog'))

def quantity_minus(request):
    current_item = OrderItem.objects.filter(id = request.GET.get('item')).first()
 
    current_item.quantity -= 1
    if current_item.quantity == 0:
        return redirect(reverse('delete_item', kwargs={'item': current_item.id}))
    else:
        current_item.price_quantity = current_item.product.price * current_item.quantity
        current_item.save()
    
        return redirect(reverse('total_price'))

def quantity_plus(request):
    current_item = OrderItem.objects.filter(id = request.GET.get('item')).first()
 
    current_item.quantity += 1
    current_item.price_quantity = current_item.product.price * current_item.quantity
    current_item.save()
    
    return redirect(reverse('total_price'))

def total_price(request):
    current_order, order_status_id = Order.objects.get_or_create(user=request.user, order_status_id=1)
    order_list = OrderItem.objects.filter(order=current_order)
    current_order.total_price = 0
    for item in order_list:
        current_order.total_price += item.price_quantity

    current_order.save()
    return redirect(reverse('cart'))


def delete_item(request, item):
    current_item = OrderItem.objects.get(id = item).delete()
    return redirect(reverse('total_price'))


def deal_order(request):
    current_order = Order.objects.filter(user=request.user, order_status_id=1).first()
    current_order.order_status_id = 2
    current_order.save()
    
    return redirect(reverse('cart'))
