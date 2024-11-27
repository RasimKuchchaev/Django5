from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html", context={"body": "<h1>Hello World!</h1>"})