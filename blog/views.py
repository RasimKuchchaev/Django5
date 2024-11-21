from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest

def index(request, id):
    people = [None, "Bob", "Sam", "Tom"]
    # если пользователь найден, возвращает его
    if id in range(1, len(people)):
        return HttpResponse(people[id])
    # если нет, возвращает ошибку 404
    return HttpResponseNotFound("Not Found")

def access(request, age):
    # если возвраст не входит в диапозон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if (age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
     

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")