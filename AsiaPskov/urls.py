"""
Definition of urls for AsiaPskov.
"""

from datetime import datetime
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # Лабы
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('feedback/', views.feedback, name='feedback'),
    path('registration/', views.registration, name='registration'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
    # Иконка
    re_path(r'^favicon\.ico$', favicon_view),

    # Каталог товаров
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:cat_id>', views.catalog, name='catalog'),

    # Корзина
    path('cart/', views.cart, name='cart'),
    path('cart/<int:message_id>', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('quantity_minus/', views.quantity_minus, name='quantity_minus'),
    path('quantity_plus/', views.quantity_plus, name='quantity_plus'),
    path(r'delete_item/(?P<item>[0-9]+)/', views.delete_item, name='delete_item'),
    path('total_price/', views.total_price, name='total_price'),
    path('deal_order/', views.deal_order, name='deal_order'),
    
    # Получение заказов и изменение для профиля пользователя
    path('orders_profile/', views.orders_profile, name='orders_profile'),
    path(r'order_details/(?P<order>[0-9]+)/', views.order_details, name='order_details'),
    path(r'order_delete/(?P<item>[0-9]+)/', views.order_delete, name='order_delete'),
    
    # Изменение заказов вподробностях о сделанном заказе
    path('quantity_minus_order/', views.quantity_minus_order, name='quantity_minus_order'),
    path('quantity_plus_order/', views.quantity_plus_order, name='quantity_plus_order'),
    path(r'total_price_order/(?P<order>[0-9]+)/', views.total_price_order, name='total_price_order'),
    path(r'switch_status_order/', views.switch_status_order, name='switch_status_order'),

    # Получить все заказы для менеджмента
    path('orders_management/', views.orders_management, name='orders_management'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
