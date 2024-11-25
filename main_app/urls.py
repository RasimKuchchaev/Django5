from django.urls import path
from main_app import views

urlpatterns = [ path("", views.index),
               path("about/", views.about),
               path("contact/", views.contact),
               path("details/", views.details),
               path("support/", views.support),
               ]