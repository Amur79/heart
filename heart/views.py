from django.http import Http404, HttpResponse
from heart.tasks import *
import datetime
from django.template import Template, Context
from django.shortcuts import render


def hello(request):
    """Пример вывода строки на страницу"""
    return HttpResponse("Hello world!")


def index(request):
    """Главная страница сайта"""
    return render(request, 'index.html', )


def current_datetime(request):
    """Текущее время"""
    now = datetime.datetime.now()
    return render(request, "nowtime.html", {'now': now})


def hours_ahead(request, offset):
    """Разница во времени"""
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>" \
           "<title> Разница времени </title>" \
           "<h3> Через %s часов будет %s </h3>" \
           "</body></html>" % (offset, dt)
    return HttpResponse(html)


def tasks(request, numtask):
    """Использование списка задача"""
    try:
        numtask = int(numtask)
    except ValueError:
        raise Http404()
    if numtask == 1:
        if 'k1' in request.GET:
            k1 = float(request.GET['k1'])
        else:
            k1 = 0
        if 'k2' in request.GET:
            k2 = float(request.GET['k2'])
        else:
            k2 = 0

        return render(request, 'task.html',
                      {'k_1': k1,
                       'k_2': k2,
                       'gip': task1(k1, k2)})
    elif numtask == 3:
        x = 5
        y = 6
        html = "<html><body>" \
            "<title> Задача № 1 </title>" \
            "<p><a href='/'>Главная страница</a></p>" \
            "<p>Вычислить гипотенузу прямоугольного треугольника. Катеты вводит пользователь. </p>" \
            "<p>Катет 1: %s </p>" \
            "<p>Катет 2: %s </p>" \
            "<p>Гипотенуза %s. </p>" \
            "</body></html>" % (x, y, task1(x, y))

    else:
        raw_template = """<html><body> 
            <title> Ошибка </title>
            <p><a href='/'>Главная страница</a></p> 
            <p>Такой задачи нет</p>
            </body></html>"""
        t = Template(raw_template)
        c = Context({})
        html = t.render(c)
        return HttpResponse(html)


def templ(request):
    """Пример использования шаблона"""
    lst = ["one", "two", "three"]

    return render(request, 'templ.html',
                  {'person_name': 'Петр Петров',
                   'company': 'Нью Текнолоджи',
                   'ship_date': datetime.date(2009, 4, 2),
                   'ordered_warranty': False,
                   'ilst': lst})  # сопоставляем список


def display_meta(request):
    """Отображение передаваемых данных Meta"""
    values = request.META.items()
    return render(request, 'dispmeta.html',
                  {'values': values})

