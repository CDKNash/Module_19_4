from django import forms


class UserRegister(forms.Form):
    name = forms.CharField(label='Введите логин', max_length=30)
    password = forms.CharField(label='Введите пароль', min_length=8)
    repeat_password = forms.CharField(label='Подтвердите пароль', min_length=8)
    age = forms.IntegerField(label='Введите свой возраст', min_value=18, max_value=120)
