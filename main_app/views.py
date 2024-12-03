from django.template.response import  TemplateResponse
from django.shortcuts import  render


def index(request):
    profile_data=['Павел', 45, '+79234567891', 'pavel@pavel.com']
    return render(request,"main_app/index.html", context={'profile_data':profile_data})

def contact(request):
    data= 'Телефон: +79123456789, E-Mail: admin@email.com'
    return render(request,"main_app/contact.html", context={"data":data})

def profile(request):
    name=request.GET.get('name', 'Дмитрий')
    age=request.GET.get('age', '39')
    phone=request.GET.get('phone', '+79123456789')
    email=request.GET.get('email', 'dmitry@email.com11')    
    return render(request,"main_app/profile.html", 
                  context={'name': name, 'age': age, 
                           'phone': phone, 'email': email})

