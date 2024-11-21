from django.urls import path, include
from blog import views



urlpatterns = [path("about/", views.about),
               path("contact/", views.contact),
               path("details/", views.details),
               path("index/<int:id>/", views.index),
               path("access/<int:age>/", views.access),
             ]