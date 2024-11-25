from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    # return render(request, 'blog/index.html')
    return TemplateResponse(request, 'blog/index.html')
