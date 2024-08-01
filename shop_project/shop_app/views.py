from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from shop_app.form import *
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required

@login_required
def buy_now(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('pid')
            product_qty = int(data.get('product_qty', 1))
            address = data.get('address')
            phone = data.get('phone')
            name=data.get('name')

            product = products_hari.objects.get(id=product_id)
            if product.quantity < product_qty:
                return JsonResponse({'status': 'Not enough stock'})

            # Create the order
            order = Order.objects.create(
                user=request.user,
                total_price=product.selling_price * product_qty,
                name=name,
                address=address,
                phone=phone
            )

            # Create the order item
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=product_qty,
                price=product.selling_price,
            )

            # Decrease the product quantity
            product.quantity -= product_qty
            product.save()

            # Redirect to order summary
            return JsonResponse({'status': 'Success', 'redirect_url': f"/order_summary/{order.id}"})

        except products_hari.DoesNotExist:
            return JsonResponse({'status': 'Product does not exist'})
        except Exception as e:
            return JsonResponse({'status': f'Error: {e}'})
    return JsonResponse({'status': 'Invalid request'})

def switch_user_form(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to switch users.")
        return redirect('login')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user != request.user:
                login(request, user)
                messages.success(request, f"Switched to user: {user.username}")
                return redirect('Home')
            else:
                messages.error(request, "You are already logged in as this user.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'product/switch_user.html')

def checkout(request):
    if not request.user.is_authenticated:
        print("1")
        return redirect('login')
    

    user_cart = cart_hari.objects.filter(user=request.user)
    if not user_cart.exists():
        messages.warning(request, "Your cart is empty")
        print("2")
        return redirect('cart')


    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        print("5")
        if form.is_valid():
            print("6")
            total_price = sum(item.product.selling_price * item.product_qty for item in user_cart)
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            order = Order.objects.create(user=request.user, total_price=total_price, name=name, address=address, phone=phone)

            for item in user_cart:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.product_qty,
                    price=item.product.selling_price * item.product_qty
                )
                item.product.quantity -= item.product_qty
                item.product.save()

            user_cart.delete()
            messages.success(request, "Order placed successfully")
            return redirect('order_summary', order_id=order.id)
        else:
            print(form.errors)  

    # Attach the first image of the product to each cart item
    for item in user_cart:
        item.product_image = item.product.images.first()

    return render(request, 'checkout/checkout.html', {'form': form, 'cart': user_cart})





def order_summary(request, order_id):
    if not request.user.is_authenticated:
        messages.success(request, "Kindly login to view Order details")
        return redirect("Home")

    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.all()
    
    for item in order_items:
        item.price_per_item = item.price / item.quantity
        item.product_image = item.product.images.first() if item.product.images.exists() else None

    return render(request, 'checkout/order_summary.html', {'order': order, 'order_items': order_items})

def home(request):
    category_names = ["Mobiles", "Home", "Fashion", "Grocery", "Electronics"]
    categories = category_hari.objects.filter(name__in=category_names)
    category_dict = {category.name: category.id for category in categories}
    mobile_category_id = category_dict.get("Mobiles")
    home_category_id = category_dict.get("Home")
    fashion_category_id = category_dict.get("Fashion")
    grocery_category_id = category_dict.get("Grocery")
    electronics_category_id = category_dict.get("Electronics")
    
    products = products_hari.objects.filter(trending=1)
    
    mobiles = products_hari.objects.filter(trending=1, category=mobile_category_id) if mobile_category_id else products_hari.objects.none()
    home = products_hari.objects.filter(trending=1, category=home_category_id) if home_category_id else products_hari.objects.none()
    fashion = products_hari.objects.filter(trending=1, category=fashion_category_id) if fashion_category_id else products_hari.objects.none()
    grocery = products_hari.objects.filter(trending=1, category=grocery_category_id) if grocery_category_id else products_hari.objects.none()
    electronics = products_hari.objects.filter(trending=1, category=electronics_category_id) if electronics_category_id else products_hari.objects.none()


    return render(request, 'shop/index.html', {
        "products": products,
        "mobiles": mobiles,
        "home": home,
        "fashion": fashion,
        "grocery": grocery,
        "electronics": electronics,
    })




def user_page(request):
    user=request.user
    return render(request,"shop/user.html",{'user':user})


def cart_page(request):
    if request.user.is_authenticated:
        cart = cart_hari.objects.filter(user=request.user)
        for item in cart:
            item.product_image = item.product.images.first()
    else:
        cart = request.session.get('cart', [])
        for item in cart:
            product = products_hari.objects.get(id=item['product_id'])
            item['product'] = product
            item['id'] = item['product_id']  # Ensure 'id' is set for the template
            # Fetch the first image related to the product
            item['product_image'] = product.images.first()
    
    return render(request, "product/cart.html", {'cart': cart})




                                                                                


def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            data = json.loads(request.body)
            product_qty = data['product_qty']
            product_id = data['pid']
            
            product_status = products_hari.objects.get(id=product_id)
            
            if product_status:
                if request.user.is_authenticated:
                    if cart_hari.objects.filter(user=request.user.id, product_id=product_id).exists():
                        messages.warning(request, "Product already in cart")
                        return JsonResponse({'status': 'Success'}, status=200)
                    else:
                        if product_status.quantity >= product_qty:
                            cart_hari.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                            messages.success(request, "Product added to cart")
                            return JsonResponse({'status': 'Success'}, status=200)
                        else:
                            messages.success(request, "Product stock not available")
                            return JsonResponse({'status': 'Success'}, status=200)
                else:
                    cart = request.session.get('cart', [])
                    for item in cart:
                        if item['product_id'] == product_id:
                            messages.success(request, "Product already in cart")
                            return JsonResponse({'status': 'Success'}, status=200)
                    
                    if product_status.quantity >= product_qty:
                        cart.append({'product_id': product_id, 'product_qty': product_qty})
                        request.session['cart'] = cart
                        messages.success(request, "Product added to cart")
                        return JsonResponse({'status': 'Success'}, status=200)
                    else:
                        messages.success(request, "Product stock not available")
                        return JsonResponse({'status': 'Success'}, status=200)
        except products_hari.DoesNotExist:
            messages.warning(request, "Product does not exist")
            return JsonResponse({'status': 'Failed'}, status=404)
        except json.JSONDecodeError:
            messages.warning(request, "Invalid data")
            return JsonResponse({'status': 'Failed'}, status=400)
    else:
        messages.warning(request, "Invalid access")
        return JsonResponse({'status': 'Failed'}, status=400)



def remove_cart(request, uid):
    if request.user.is_authenticated:
        try:
            # Fetch the cart item or return a 404 error if not found
            cartitem = cart_hari.objects.get(id=uid, user=request.user)
            cartitem.delete()
            messages.success(request, "Item removed from cart")
        except cart_hari.DoesNotExist:
            messages.error(request, "Item not found in your cart")
        except cart_hari.MultipleObjectsReturned:
            messages.error(request, "Multiple items found with the same ID, please contact support")
    else:
        cart = request.session.get('cart', [])
        # Look for the item in the session cart
        updated_cart = [item for item in cart if item['product_id'] != uid]
        if len(updated_cart) < len(cart):
            request.session['cart'] = updated_cart
            messages.success(request, "Item removed from cart")
        else:
            messages.error(request, "Item not found in your cart")
    
    return redirect("cart")


def fav_view(request):
    if request.user.is_authenticated:
        fav = favourite_hari.objects.filter(user=request.user)
        for item in fav:
            item.product_image = item.product.images.first()
    else:
        fav = request.session.get('favourites', [])
        for item in fav:
            product = products_hari.objects.get(id=item['product_id'])
            item['product'] = product
            item['id'] = item['product_id']  # Set the ID for the template
            item['product_image'] = product.images.first()
    
    return render(request, "product/favourite.html", {'fav': fav})



def fav_page(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            data = json.loads(request.body)
            product_id = data['pid']
            
            product_status = products_hari.objects.get(id=product_id)
            
            if product_status:
                if request.user.is_authenticated:
                    if favourite_hari.objects.filter(user=request.user.id, product_id=product_id).exists():
                        messages.success(request, "Product already in favourites")
                        return JsonResponse({'status': 'Success'}, status=200)
                    else:
                        favourite_hari.objects.create(user=request.user, product_id=product_id)
                        messages.success(request, "Product added to favourites")
                        return JsonResponse({'status': 'Success'}, status=200)
                else:
                    favourites = request.session.get('favourites', [])
                    for item in favourites:
                        if item['product_id'] == product_id:
                            messages.success(request, "Product already in favourites")
                            return JsonResponse({'status': 'Success'}, status=200)
                    
                    favourites.append({'product_id': product_id})
                    request.session['favourites'] = favourites
                    messages.success(request, "Product added to favourites")
                    return JsonResponse({'status': 'Success'}, status=200)
        except products_hari.DoesNotExist:
            messages.error(request, "Product does not exist")
            return JsonResponse({'status': 'Failed'}, status=404)
        except json.JSONDecodeError:
            messages.error(request, "Invalid data")
            return JsonResponse({'status': 'Failed'}, status=400)
    else:
        messages.error(request, "Invalid access")
        return JsonResponse({'status': 'Failed'}, status=400)



def remove_fav(request, fid):
    if request.user.is_authenticated:
        try:
            favitem = favourite_hari.objects.get(id=fid, user=request.user)
            favitem.delete()
            messages.success(request, "Item removed from favourites")
        except favourite_hari.DoesNotExist:
            messages.error(request, "Item not found in your favourites")
        except favourite_hari.MultipleObjectsReturned:
            messages.error(request, "Multiple items found with the same ID, please contact support")
    else:
        favourites = request.session.get('favourites', [])
        updated_favourites = [item for item in favourites if item['product_id'] != fid]
        if len(updated_favourites) < len(favourites):
            request.session['favourites'] = updated_favourites
            messages.success(request, "Item removed from favourites")
        else:
            messages.error(request, "Item not found in your favourites")
    
    return redirect("fav_view")



def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect("/")



def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    next_url = request.GET.get('next', '/')
    
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=name, password=pwd)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In successfully")
            
            # Migrate session cart to user's cart
            session_cart = request.session.get('cart', [])
            for item in session_cart:
                product_id = item['product_id']
                product_qty = item['product_qty']
                if not cart_hari.objects.filter(user=request.user, product_id=product_id).exists():
                    cart_hari.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)

            session_favourites = request.session.get('favourites', [])
            for item in session_favourites:
                product_id = item['product_id']
                if not favourite_hari.objects.filter(user=request.user, product_id=product_id).exists():
                    favourite_hari.objects.create(user=request.user, product_id=product_id)
            
            request.session['favourites'] = []
            request.session['cart'] = []

            return redirect(next_url)
        else:
            messages.error(request, "Invalid User Name or password")
            return redirect(f"/login?next={next_url}")
    
    return render(request, 'product/login.html', {'next': next_url})


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