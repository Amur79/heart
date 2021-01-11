import joblib
import numpy as np
import pandas as pd

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
    model_art = joblib.load('cardform/arter-modelRF.model')
    # Получаем вероятности заболевания, на вход подаем массив pd.DataFrame([d])
    y_pred_art = model_art.predict_proba(X)[:,1]
    return y_pred_art

def onmk_predict(X):
    # ОНМК
    model_ONMK = joblib.load('cardform/ОНМК-modelRF.model')
    y_pred_ONMK = model_ONMK.predict_proba(X)[:,0] / 0.93 * 0.5
    return y_pred_ONMK
    
def steno_predict(X):
    # Стенокардия, ИБС, инфаркт миокарда
    model_steno = joblib.load('cardform/steno-modelRF.model')
    y_pred_steno = model_steno.predict_proba(X)[:,0] / 0.91 * 0.5
    return y_pred_steno
    
def heart_predict(X):
    # Сердечная недостаточность
    model_heart = joblib.load('cardform/heart-modelRF.model')
    y_pred_heart = model_heart.predict_proba(X)[:,1] / 0.91 * 0.5
    return y_pred_heart
    