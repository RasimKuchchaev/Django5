from django.urls import path, re_path
from blog import views

urlpatterns = [path('', views.index),
               path('about/', views.about, kwargs={"name":"Tom", "age":38}),
               re_path(r"^contact/", views.contact),
               path('user/<str:name>/<int:age>/', views.user),
               path('user/<str:name>/', views.user),
               path('user/', views.user),
               path('message/<str:category>/<str:subcategory>/<str:theme>/<int:number>', views.message)
               ]