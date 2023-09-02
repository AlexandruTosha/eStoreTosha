from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1> eStoreTosha - Index Page </h1>")
    return render(request, "home.html", {})

def cart_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1> eStoreTosha - Cart Page </h1>")
    return render(request, "cart.html", {})

def user_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1> eStoreTosha - User Page </h1>")
    return render(request, "users.html", {})

def products_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1> eStoreTosha - Products Page </h1>")
    return render(request, "products.html", {})