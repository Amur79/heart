from django import forms

class CardForm(forms.Form):

    Holesterin = forms.CharField(max_length=20, label='Холестерин', help_text='Уровень холестерина')  # Холестерин
    Vozrast = forms.IntegerField(label='Возраст', help_text='Ваш возраст, лет')  # Возраст
    Ves = forms.IntegerField(label='Вес', help_text='Ваш вес, кг')  # Вес
    Rost = forms.IntegerField(label='Рост', help_text='Ваш рост, см')  # Рост
    Glukoza = forms.CharField(max_length=20, label='Глюкоза', help_text='Уровень глюкозы')  # Глюкоза
    Sex = forms.IntegerField(required=1, label='Пол', help_text='М - 1, Ж - 0')  # Пол
    Obitanie = forms.IntegerField(required=1, label='Место проживания', help_text='1- город, 2- село')  # Город, село
    Dostatok = forms.IntegerField(required=2, label='Достаток', help_text='очень низкий - 0, Низкий - 1, средний - 2, высокий - 3')  # Достаток по срав с друг
    Kyrit = forms.IntegerField(required=1, label='Курите', help_text='Да - 1, нет - 0')  # Курит или нет
    Alkogol = forms.IntegerField(required=1, label='Выпиваете', help_text='Да - 1, нет - 0')  # Алкоголь употребляет
