from django.urls import path, include
from blog import views
from django.views.generic import TemplateView



urlpatterns = [path("", views.index),  
               path("about/", TemplateView.as_view(template_name="blog/about.html", extra_context={'header':"О сайте"})),  
               path("contact/", TemplateView.as_view(template_name="blog/contact.html"))         
             ]