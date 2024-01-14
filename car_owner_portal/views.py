from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from car_owner_portal.models import *
from customer_portal.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'car_owner/login.html')
    else:
        return render(request, 'car_owner/home_page.html')

def login(request):
    return render(request, 'car_owner/login.html')


def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'car_owner/home_page.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            car_owner = CarOwner.objects.get(car_owner = user)
        except:
            car_owner = None
        if car_owner is not None:
            auth.login(request, user)
            return render(request, 'car_owner/home_page.html')
        else:
            return render(request, 'car_owner/login_failed.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'car_owner/login.html')

def register(request):
    return render(request, 'car_owner/register.html')

def registration(request):
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    city = request.POST['city']
    city = city.lower()
    district = request.POST['district']

    try:
        user = User.objects.create_user(username = username, password = password, email = email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
        return render(request, 'car_owner/registration_error.html')
    try:
        area = Area.objects.get(city = city, district = district)
    except:
        area = None
    if area is not None:
        car_owner = CarOwner(car_owner = user, mobile = mobile, area=area)
    else:
        area = Area(city = city, district = district)
        area.save()
        area = Area.objects.get(city = city, district = district)
        car_owner = CarOwner(car_owner = user, mobile = mobile, area=area)
    car_owner.save()
    return render(request, 'car_owner/registered.html')

@login_required
def add_vehicle(request):
    car_name = request.POST['car_name']
    color = request.POST['color']
    cd = CarOwner.objects.get(car_owner=request.user)
    city = request.POST['city']
    city = city.lower()
    district = request.POST['district']
    district = district.lower()
    description = request.POST['description']
    capacity = request.POST['capacity']
    try:
        area = Area.objects.get(city = city, district = district)
    except:
        area = None
    if area is not None:
        car = Vehicles(car_name=car_name, color=color, owner=cd, area = area, description = description, capacity=capacity)
    else:
        area = Area(city = city, district = district)
        area.save()
        area = Area.objects.get(city = city, district = district)
        car = Vehicles(car_name=car_name, color=color, owner=cd, area = area,description=description, capacity=capacity)
    car.save()
    return render(request, 'car_owner/vehicle_added.html')

@login_required
def manage_vehicles(request):
    username = request.user
    user = User.objects.get(username = username)
    car_owner = CarOwner.objects.get(car_owner = user)
    vehicle_list = []
    vehicles = Vehicles.objects.filter(owner = car_owner)
    for v in vehicles:
        vehicle_list.append(v)
    return render(request, 'car_owner/manage.html', {'vehicle_list':vehicle_list})

@login_required
def order_list(request):
    username = request.user
    user = User.objects.get(username = username)
    car_owner = CarOwner.objects.get(car_owner = user)
    orders = Orders.objects.filter(car_owner = car_owner)
    order_list = []
    for o in orders:
        if o.is_complete == False:
            order_list.append(o)
    return render(request, 'car_owner/order_list.html', {'order_list':order_list})

@login_required
def complete(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    vehicle = order.vehicle
    order.is_complete = True
    order.save()
    vehicle.is_available = True
    vehicle.save()
    return HttpResponseRedirect('/car_owner_portal/order_list/')


@login_required
def history(request):
    user = User.objects.get(username = request.user)
    car_owner = CarOwner.objects.get(car_owner = user)
    orders = Orders.objects.filter(car_owner = car_owner)
    order_list = []
    for o in orders:
        order_list.append(o)
    return render(request, 'car_owner/history.html', {'wallet':car_owner.wallet, 'order_list':order_list})

@login_required
def delete(request):
    veh_id = request.POST['id']
    vehicle = Vehicles.objects.get(id = veh_id)
    vehicle.delete()
    return HttpResponseRedirect('/car_owner_portal/manage_vehicles/')
