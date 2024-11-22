from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    return HttpResponse("Index")


def about(request):
    return HttpResponsePermanentRedirect("/")


def contact(request):
    return HttpResponseRedirect("/about/")


def details(request):
    return HttpResponsePermanentRedirect("/")

def support(request):
    return HttpResponseRedirect("/contact/")