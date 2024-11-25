from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
