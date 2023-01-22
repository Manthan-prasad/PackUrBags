from atexit import register
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create your views here.
from .models import *
# from .forms import OrderForm, CreateUserForm
# from .filters import OrderFilter


def store(request):
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    # name = models.Charfield(max_length = 200)
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 }
        cartItems = order['get_cart_items']

    packages = Package.objects.all()
    context = {'packages':packages, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)
    

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 }
        cartItems = order['get_cart_items']
    packages = Package.objects.all()
    context = {'items':items , 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        datas=[]
        for i in range(1,cartItems+1):
            datas.append(i)
            

    else:
        items = []
        datas=[]
        order = {'get_cart_total':0, 'get_cart_items':0 }
        cartItems = order['get_cart_items']
    context = {'items':items , 'order':order,'cartItems':cartItems,'datas':datas}
    return render(request, 'store/checkout.html', context)

# def registerPage(request):
    # form=UserCreationForm()

    # if request.method == 'POST':
    #     form=UserCreationForm()
    #     if form.is_valid():
    #         form.save()

    # context={}
    # return render(request, 'store/register.html', context)

# def loginPage(request):
#     context={}
#     return render(request, 'store/login.html', context)

def updateItem(request):
	data = json.loads(request.body)
	packageId = data['packageId']
	action = data['action']
	print('Action:', action)
	print('Package:', packageId)

	customer = request.user.customer
	package = Package.objects.get(id=packageId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(oder=order, package=package)

	if orderItem.quantity == None:
		orderItem.quantity = 0

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

    

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def view(request, packageId):
    package = Package.objects.get(id=packageId)
    context = {'package': package}
    return render(request, 'store/view.html', context)

def home(request):
    context={}
    return render(request, 'store/home.html', context)

def processOrder(request):
    print('Data:',request.body)
    return JsonResponse('Payment complete!',safe=False)



from django.shortcuts import render, redirect



# def loginPage(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, 'store/store.html')
#         else:
#             return render(request, 'store/login.html', {'error': 'Invalid login credentials. Please try again.'})
#     else:
    # return render(request, 'store/login.html')

# def logout_view(request):
#     logout(request)
#     return redirect('store')
