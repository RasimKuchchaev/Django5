from django.urls import path, include
from blog import views
from django.views.generic import TemplateView



urlpatterns = [path("", views.index),  
               path("about/", views.about),          
             ]