"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from heart.views import *
from cardform.views import *
from books.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),  # админ панель
    url(r'^$', index),  # главная страница
    url(r'^hello/$', hello),  # просто привет
    url(r'^cdt/$', current_datetime),  # текущее время
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),  # сдвиг на от 1 до 99 часов
    url(r'^tasks/(\d{1,2})/$', tasks),  # переход по номеру задачи
    url(r'^templ/$', templ),  # использование шаблона
    url(r'^heart/$', heart),  # показ данных запроса
    url(r'search/$', search),  # результат поиска
    url(r'^cardform/$', cardform), # Карточка ввода данных
    url(r'^calculation$', calculation),  # Вывод результатов расчета
]

