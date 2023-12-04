"""
Definition of forms.
"""

from email import message
from tkinter.ttk import Style
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment

from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
    
class FeedbackForm(forms.Form):
    """Форма обратной связи"""
    name = forms.CharField(label='Ваше имя', min_length=3, max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Артём"}))
    gender = forms.ChoiceField(label='Ваш пол', 
                               choices=[('1','Мужчина'),('2','Женщина')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check form-check-inline'})
                               ,initial=1)
    age = forms.ChoiceField(label='Сколько вам лет?',
                                choices=(('1','0-17'),
                                        ('2','18-25'),
                                        ('3','26-39'),
                                        ('4','40+')),
                                widget=forms.Select(attrs={'class': 'form-select form-select-lg'}),
                                initial=1)
    message = forms.CharField(label='Напишите ваши замечания или советы для улучшения заведения',
                             widget=forms.Textarea(attrs={'row':12,'cols':20,'class': 'form-control', 'placeholder':"Мне не понравилось ... "}))
    email = forms.EmailField(label='Ваш Email', min_length=3, max_length=40,
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"name@example.com"}))
    

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text
        widgets ={
            'text': forms.Textarea(attrs={'row':12,'cols':20, 'class': 'form-control'}),
        }
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','content','image')
        labels = {'title':"Заголовок",'description':"Краткое содержание",'content':"Полное содержание",'image':"Картинка"}
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Название"}),
            'description': forms.Textarea(attrs={'row':4,'cols':10, 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'row':12,'cols':20, 'class': 'form-control'}),
        }