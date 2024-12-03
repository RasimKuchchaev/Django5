from django.template.response import  TemplateResponse
from django.shortcuts import  render


def index(request):
    user_list = [{'name': 'Дмитрий', 'experience': 9},
                {'name': 'Павел',   'experience': 5},
                {'name': 'Алексей', 'experience': 3},
                {'name': 'Иван',    'experience': 0},
                {'name': 'Денис',   'experience': 2},
                {'name': 'Игорь',   'experience': 7},
                {'name': 'Руслан',  'experience': 1},
                {'name': 'Евгений', 'experience': 4},
                {'name': 'Андрей',  'experience': 2},
                {'name': 'Николай', 'experience': 8}]
    return render(request,"main_app/index.html", context={'user_list':user_list, 'tmpl_name':'main_app/employees_list.html'})

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

