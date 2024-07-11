from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from shop_app.form import *
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    products=Products_Hari.objects.filter(trending=1)
    return render(request,'shop/index.html',{"products":products})

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart_hari.objects.filter(user=request.user)
        return render(request,"product/cart.html",{'cart':cart})
    else:
        return redirect('/')
    

def remove_cart(request,uid):
   cartitem=Cart_hari.objects.get(id=uid)
   cartitem.delete()
   return redirect("cart")


def fav_view(request):
    if request.user.is_authenticated:
        fav=Favourite_hari.objects.filter(user=request.user)
        return render(request,"product/favourite.html",{'fav':fav})
    else:
        return redirect('/')

def fav_page(request):
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_authenticated:
                data=json.load(request)
                product_id=data['pid']
                product_status=Products_Hari.objects.get(id=product_id)
                if product_status:
                    if Favourite_hari.objects.filter(user=request.user.id,product_id=product_id):
                        return JsonResponse({'status':'product already in favourite'},status=200)
                    else:
                        Favourite_hari.objects.create(user=request.user,product_id=product_id)
                        return JsonResponse({'status':'product added to favourite'},status=200)
            else:
                return JsonResponse({'status':'login to add favourite'},status=200)
        else:
            return JsonResponse({'status':'Invalid Access'},status=200)  
        
def remove_fav(request,fid):
   favitem=Favourite_hari.objects.get(id=fid)
   favitem.delete()
   return redirect("fav_view")


def add_to_cart(request):
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_authenticated:
                data=json.load(request)
                product_qty=data['product_qty']
                product_id=data['pid']
                # print(request.user.id)

                product_status=Products_Hari.objects.get(id=product_id)
                if product_status:
                    if Cart_hari.objects.filter(user=request.user.id,product_id=product_id):
                        return JsonResponse({'status':'product already incart'},status=200)
                    else:
                       if product_status.quantity>=product_qty:
                           Cart_hari.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                           return JsonResponse({'status':'product Added to incart'},status=200)
                       else:
                           return JsonResponse({'status':'product stock not available'},status=200)
            else:
                return JsonResponse({'status':'login to add cart'},status=200)
        else:
            return JsonResponse({'status':'Invalid Access'},status=200)                                                                                    

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
    category=Category_Hari.objects.filter(status=0)
    return render(request,'shop/collections.html',{'category':category})

def collectionview(request, name):
    if Category_Hari.objects.filter(status=0, name=name).exists():
        products = Products_Hari.objects.filter(category__name=name)
        return render(request, 'product/index.html', {'products': products,'category':name})
    else:
        messages.warning(request, "No such Category found!!!")
        return redirect('Collection')
    
def product_details(request,cname,pname):
    if (Category_Hari.objects.filter(status=0, name=cname)):
        if (Products_Hari.objects.filter(status=0, name=pname)):
            products=Products_Hari.objects.filter(name=pname,status=0).first()
            return render(request,"product/product_details.html",{"products":products})
        else:
            messages.warning(request, "No such Category found!!!")
            return redirect('Collection')
    else:
        messages.error(request, "No such Product found!!!")
        return redirect('Collection')
    