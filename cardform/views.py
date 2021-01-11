from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from cardform import heart_model
from cardform.forms import CardForm

import joblib
import numpy as np
import pandas as pd

def cardform(request):
    """Карточка ввода данных"""
    formin = CardForm()
    return render(request, 'cardform.html', {'form': formin})

def calculation(request):
    """ Вывод результатов расчетов """

    formout = CardForm(request.POST)
    if request.method == 'POST':
        formout = CardForm(request.POST)
        d = {}
        if formout.is_valid():

            Holesterin = float(request.POST.get('Holesterin'))
            Vozrast = int(request.POST.get('Vozrast'))
            Ves_Rost = str(int(request.POST.get('Ves'))/int(request.POST.get('Rost')))
            Glukoza = float(request.POST.get('Glukoza'))
            Sex = int(request.POST.get("Sex"))
            Obitaniye = int(request.POST.get('Obitanie'))
            Dostatok = int(request.POST.get('Dostatok'))
            Kyrit = int(request.POST.get('Kyrit'))
            Alkogol = int(request.POST.get('Alkogol'))

            d = {'Возраст': Vozrast, 'Вес/рост': Ves_Rost, 'Глюкоза': Glukoza, 'Пол': Sex,
                 'Место проживания 1-город 2-село': Obitaniye, 'Достаток по срав с друг': Dostatok}
            X = pd.DataFrame([d])
            data_art = heart_model.art_predict(X)

            d = {'Возраст': Vozrast, 'Холестерин': Holesterin, 'Пол': Sex, 'smoke': Kyrit,
                 'Достаток по срав с друг': Dostatok, 'Alcohol': Alkogol}
            X = pd.DataFrame([d])
            data_onmk = heart_model.onmk_predict(X)

            d = {'Возраст': Vozrast, 'Глюкоза': Glukoza, 'Место проживания 1-город 2-село': Obitaniye, 'smoke': Kyrit,
                 'Достаток по срав с друг': Dostatok}
            X = pd.DataFrame([d])
            data_steno = heart_model.steno_predict(X)

            d = {'Возраст': Vozrast, 'Глюкоза': Glukoza, 'Холестерин': Holesterin, 'Пол': Sex, 'smoke': Kyrit,
                 'Достаток по срав с друг': Dostatok}
            X = pd.DataFrame([d])
            data_heart = heart_model.heart_predict(X)

            rekomend = 'Ведите здоровый образ жизни'
            if Kyrit == 1:
                rekomend = rekomend + '\nРекомендуем бросить курить!'
            if Alkogol == 1:
                rekomend = rekomend + '\nРекомендуем снизить употребление алкоголя!'

            context = {"data_art": data_art,
                       "data_onmk": data_onmk,
                       "data_steno": data_steno,
                       "data_heart": data_heart,
                       "rekomend": rekomend}
            return render(request, "heart.html", context=context)
            return HttpResponseRedirect('/calculation')
    else:
        formout = CardForm()
    return render(request, 'calculation.html',
                  {'formout': formout})


# Просто тестовые данные, в релизе не нужны
"""
d = {'Возраст': 56,'Вес/рост': 0.499405,'Глюкоза': 4.9, 'Пол': False,
'Место проживания 1-город 2-село': False, 'Достаток по срав с друг': 2}
X = pd.DataFrame([d])
"""

"""# Артериальная гипертензия
# Возраст - число, вес поделённый на рост, глюкоза - дробное число, пол - 1 если мужской, 0 женский, 
# Место 1 если город 0 если деревня, достаток 0, 1, 2, 3 или 4 (от бомжа до очень высокого)
# Алкоголь - 1 или 0 (в данный момент), smoke - курение 1 или 0
x_art = data_raw[['Возраст', 'Вес/рост', 'Глюкоза', 'Пол', 'Место проживания 1-город 2-село', 
                  'Достаток по срав с друг']]
# ОНМК
x_ONMK = data_raw[['Возраст', 'Холестерин', 'Пол', 'smoke', 'Достаток по срав с друг', 'Alcohol']]
# Стенокардия, ИБС, инфаркт миокарда
x_steno = data_raw[['Возраст', 'Глюкоза', 'Место проживания 1-город 2-село', 'smoke', 'Достаток по срав с друг']]
# Сердечная недостаточность
x_heart = data_raw[['Возраст', 'Глюкоза', 'Холестерин', 'Пол', 'smoke', 'Достаток по срав с друг']]
#Прочие заболевания сердца
x_else = data_raw[['Возраст', 'Холестерин', 'Пол', 'Достаток по срав с друг']]
"""


def art_predict(X):
    # Артериальная гипертензия
    model_art = joblib.load('arter-modelRF.model')
    # Получаем вероятности заболевания, на вход подаем массив pd.DataFrame([d])
    y_pred_art = model_art.predict_proba(X)[:, 1]
    return y_pred_art


def onmk_predict(X):
    # ОНМК
    model_ONMK = joblib.load('ОНМК-modelRF.model')
    y_pred_ONMK = model_ONMK.predict_proba(X)[:, 0] / 0.93 * 0.5
    return y_pred_ONMK


def steno_predict(X):
    # Стенокардия, ИБС, инфаркт миокарда
    model_steno = joblib.load('steno-modelRF.model')
    y_pred_steno = model_steno.predict_proba(X)[:, 0] / 0.91 * 0.5
    return y_pred_steno


def heart_predict(X):
    # Сердечная недостаточность
    model_heart = joblib.load('heart-modelRF.model')
    y_pred_heart = model_heart.predict_proba(X)[:, 1] / 0.91 * 0.5
    return y_pred_heart

def heart(request):
    data = ""
    d = {}
    if "age" in request.GET:
        d['Возраст'] = request.GET['age']
    d = {'Возраст': 56,'Вес/рост': 0.499405,'Глюкоза': 4.9, 'Пол': False, 'Место проживания 1-город 2-село': False, 'Достаток по срав с друг': 2}
    X = pd.DataFrame([d])
    data = heart_model.art_predict(X)
    context = {"data": data}
    return render(request, "heart.html", context=context)