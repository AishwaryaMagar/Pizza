from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel, CustomerModel, OrderModel
from django.contrib.auth.models import User
import re 

# Create your views here.


def adminLoginView(request):
    return render(request, "pizzaapp/login.html")


def authenticateAdmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None and user.username == 'Tanvi':
        login(request, user)
        return redirect('adminHomePage')
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('adminLoginPage')

def adminHomePageView(request):
    context = {'pizzas': PizzaModel.objects.all()}
    return render(request, 'pizzaapp/adminhome.html', context)


def logoutadmin(request):
    logout(request)
    return redirect('adminLoginPage')


def addPizza(request):
    name = request.POST['Pizza']
    price = request.POST['Price']

    PizzaModel(name=name, price=price).save()
    return redirect('adminHomePage')


def deletePizza(request, pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminHomePage')


def homePageView(request):
    return render(request, 'pizzaapp/homepage.html')


def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,email):
        return 1
    else :
        return 0

def checkphone(phoneno):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    if Pattern.match(phoneno):
        return 1
    else:
        return 0


def signUpUser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']
    email = request.POST['email']

    if User.objects.filter(username=username).exists():
        messages.add_message(request, messages.ERROR, "User already exists")
        return redirect('homePage')

    if len(username) == 0 and len(username) < 5 :
        messages.add_message(request, messages.ERROR, "USername should not be empty and Minimum 5 characters required")
        return redirect('homePage')
              
    if len(password) < 2:
        messages.add_message(request, messages.ERROR, "Password Should Contain a minimum of 5 characters")
        return redirect('homePage')

    val_email = check(email)
    if val_email == 0:
        messages.add_message(request, messages.ERROR, "INVALID EMIAL")
        return redirect('homePage')

    val_phone = checkphone(phoneno)
    if val_phone == 0:
        messages.add_message(request, messages.ERROR, "INVALID PHONE NO")
        return redirect('homePage')

 

    
    

    User.objects.create_user(username=username, password=password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(userid=User.objects.all()[
                  int(lastobject)].id, phoneno=phoneno, email=email).save()
    messages.add_message(request, messages.ERROR, "User Successfully Created")
    return redirect('homePage')


def authenticateUser(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('customerpage')
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('userloginpage')


def userLoginView(request):
    return render(request, "pizzaapp/userlogin.html")


def customerview(request):
    username = request.user.username
    context = {'username': username, 'pizzas': PizzaModel.objects.all()}
    return render(request, 'pizzaapp/customerview.html', context)


def userlogout(request):
    logout(request)
    return redirect('userloginpage')


def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')

    print(request.user.id)
    username = request.user.username
    phoneno = CustomerModel.objects.filter(userid=request.user.id)[0].phoneno
    address = request.POST['address']
    if len(address)<1:
        messages.add_message(request, messages.ERROR, "Please enter address !!")
        return redirect('customerpage')
    email = CustomerModel.objects.filter(userid=request.user.id)[0].email
    ordereditems = ""
    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        name = pizza.name
        price = pizza.price

        quantity = request.POST.get(str(pizzaid), " ")
        print(name)
        print(price)
        print(quantity)
        if str(quantity) != "0" and str(quantity) != " ":
            ordereditems = ordereditems + name+" " + "price : " + \
                str(int(quantity)*int(price)) + " " + \
                "quantity : " + quantity+"    "

    print(ordereditems)
    OrderModel(username=username, phoneno=phoneno, address=address,
               email=email, ordereditems=ordereditems).save()  
    messages.add_message(request, messages.ERROR, "order succesfully placed")
    return redirect('customerpage')

def userorder(request):
    orders = OrderModel.objects.filter(username = request.user.username)
    context = {'orders': orders}
    return render(request, 'pizzaapp/userorder.html', context)

def adminorders(request):
    orders = OrderModel.objects.all()
    context = {'orders': orders}
    return render(request, 'pizzaapp/adminorder.html', context)

def acceptorder(request, orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "Accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])

def declineorder(request, orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "Declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])