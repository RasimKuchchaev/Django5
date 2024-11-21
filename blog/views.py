from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страница")

def products(request, id):
    return HttpResponse(f"Товар {id}")

def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")

def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")

def new(request):
    return HttpResponse("Новые товары")

def top(request):
    return HttpResponse("Наиболее популярные товары")

def about(request, name, age):
    return HttpResponse(f"""<h2>О сайте</h2>
                        <p>Имя: {name}</p>
                        <p>Возраст: {age}</p>""")

def contact(request):
    return HttpResponse("<h1>Контакты</h1>")

def user(request, name='Undefined', age=0):
    return HttpResponse(f'<h1>Name: {name} <br> Age: {age}</h1>')

def message(request, category, subcategory, theme, number):
    return HttpResponse(f'''<h2>Сообщение</h2> 
                        <ul>
                            <li>category: {category}</li>
                            <li>subcategory: {subcategory}</li>
                            <li>theme: {theme}</li>
                            <li>number: {number}</li>
                        </ul>
''')
