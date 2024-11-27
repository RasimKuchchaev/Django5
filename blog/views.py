from django.shortcuts import render


def index(request):
    # if
    data = {"age": 40}
    # return render(request, "blog/index.html", context=data)

    # for
    cat = ["Python", "Java", "C++", "C#", "Kotlin", "Go", "Rust", "JS", "PHP"]
    return render(request, "blog/index.html", context={"cat": cat, "age": data})