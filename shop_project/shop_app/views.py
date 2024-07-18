from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from shop_app.form import *
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    products=products_hari.objects.filter(trending=1)
    return render(request,'shop/index.html',{"products":products})

def cart_page(request):
    if request.user.is_authenticated:
        cart=cart_hari.objects.filter(user=request.user)
        return render(request,"product/cart.html",{'cart':cart})
    else:
        messages.warning(request,"Kindly Log In to view Cart")
        return redirect('/')


def add_to_cart(request):
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_authenticated:
                data=json.load(request)
                product_qty=data['product_qty']
                product_id=data['pid']
                # print(request.user.id)

                product_status=products_hari.objects.get(id=product_id)
                if product_status:
                    if cart_hari.objects.filter(user=request.user.id,product_id=product_id):
                        return JsonResponse({'status':'product already incart'},status=200)
                    else:
                       if product_status.quantity>=product_qty:
                           cart_hari.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                           return JsonResponse({'status':'product Added to incart'},status=200)
                       else:
                           return JsonResponse({'status':'product stock not available'},status=200)
            else:
                return JsonResponse({'status':'login to add cart'},status=200)
        else:
            return JsonResponse({'status':'Invalid Access'},status=200)                                                                                    


def remove_cart(request,uid):
   cartitem=cart_hari.objects.get(id=uid)
   cartitem.delete()
   return redirect("cart")


def fav_view(request):
    if request.user.is_authenticated:
        fav=favourite_hari.objects.filter(user=request.user)
        return render(request,"product/favourite.html",{'fav':fav})
    else:
        messages.warning(request,"Kindly Log In to view favourites")
        return redirect('/')

def fav_page(request):
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_authenticated:
                data=json.load(request)
                product_id=data['pid']
                product_status=products_hari.objects.get(id=product_id)
                if product_status:
                    if favourite_hari.objects.filter(user=request.user.id,product_id=product_id):
                        return JsonResponse({'status':'product already in favourite'},status=200)
                    else:
                        favourite_hari.objects.create(user=request.user,product_id=product_id)
                        return JsonResponse({'status':'product added to favourite'},status=200)
            else:
                return JsonResponse({'status':'login to add favourite'},status=200)
        else:
            return JsonResponse({'status':'Invalid Access'},status=200)  
        
def remove_fav(request,fid):
   favitem=favourite_hari.objects.get(id=fid)
   favitem.delete()
   return redirect("fav_view")



def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect("/")



def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged In successfully")
            else:
                messages.error(request,"Invalid User Name or password")
                return redirect("/login")
        return render(request,'product/login.html')

def register(request):
    form=CustomuserForm()
    if request.method=="POST":
        form=CustomuserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull.You Can Login now")
            return redirect("/login")
    return render(request,'shop/register.html',{'form':form})

def collections(request):
    category=category_hari.objects.filter(status=0)
    return render(request,'shop/collections.html',{'category':category})

def collectionview(request, name):
    if category_hari.objects.filter(status=0, name=name).exists():
        products = products_hari.objects.filter(category__name=name)
        return render(request, 'product/index.html', {'products': products,'category':name})
    else:
        messages.warning(request, "No such Category found!!!")
        return redirect('Collection')
    
def product_details(request,cname,pname):
    if (category_hari.objects.filter(status=0, name=cname)):
        if (products_hari.objects.filter(status=0, name=pname)):
            products=products_hari.objects.filter(name=pname,status=0).first()
            return render(request,"product/product_details.html",{"products":products})
        else:
            messages.warning(request, "No such Category found!!!")
            return redirect('Collection')
    else:
        messages.error(request, "No such Product found!!!")
        return redirect('Collection')
    