"""
Definition of forms.
"""

from email import message
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment

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
    name = forms.CharField(label='Ваше имя', min_length=3, max_length=20)
    gender = forms.ChoiceField(label='Ваш пол', 
                               choices=[('1','Мужчина'),('2','Женщина')],
                               widget=forms.RadioSelect,initial=1)
    notice = forms.BooleanField(label='Вам нравится наш ассортимент суши?',
                                required=True)
    delivery = forms.ChoiceField(label='Сколько раз в месяц вызаказываете доставку еды?',
                                 choices=(('1','1-3'),
                                          ('2','4-6'),
                                          ('3','7-9'),
                                          ('4','Больше 9 раз в месяц')), initial=1)
    message = forms.CharField(label='Напишите ваши замечания или советы для улучшения заведения',
                             widget=forms.Textarea(attrs={'row':12,'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text