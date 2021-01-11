from django.shortcuts import render
from books.models import Book

# Create your views here.


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:  # пустой запрос
            errors.append('Введите поисковый запрос.')
        elif len(q) > 20: # длина запроса больше 20 символов
            errors.append('Введите не более 20 символов.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_result.html',
                          {'books': books,
                           'query': q})

    return render(request, 'search_form.html',
                  {'errors': errors})
