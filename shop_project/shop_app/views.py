from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib import messages
from shop_app.form import *
from django.contrib.auth import authenticate,logout,login, update_session_auth_hash
from django.http import JsonResponse
import json
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.core.cache import cache
from .tasks import send_order_confirmation_email  
import time 
from log_module.logging_config import setup_logging

logger = setup_logging()





## With Redis 

# def collections(request):
#     start_time = time.time()  
#     try:
#         categories = cache.get('category_list')
#         logger.info("Categories fetched from cache.")
#         if not categories:
#             categories = category_hari.objects.filter(hari=0)
#             cache.set('category_list', categories, timeout=900)
#             logger.info("Categories fetched from database and set in cache.")
#     except Exception as e:
#         logger.error(f"An error occurred while fetching categories: {str(e)}",exc_info=True)
    
#     end_time = time.time() 
#     time_taken = end_time - start_time
#     logger.info(f"Time taken to fetch categories: {time_taken:.4f} seconds")
    
#     return render(request, 'shop/collections.html', {'category': categories})


## without redis

def collections(request):
    start_time = time.time()  
    try:
        categories = cache.get('category_list')
        logger.info("Categories fetched from cache.")
    
        if not categories:
            categories = category_hari.objects.filter(status=0)
            cache.set('category_list', categories, timeout=900)
            logger.info("Categories fetched from database and set in cache.")
    except Exception as e:
        logger.exception(f"An error occurred while fetching categories: {str(e)}")
    
    end_time = time.time() 
    time_taken = end_time - start_time
    logger.info(f"Time taken to fetch categories: {time_taken:.4f} seconds")
    
    return render(request, 'shop/collections.html', {'category': categories})



def view_wishlist(request):
    try:
        if request.user.is_authenticated:
            wishlist, created = Wishlist.objects.get_or_create(user=request.user, name='My Wishlist')
            
            items = wishlist.items.all()
            logger.info(f"Wishlist created. Number of items in wishlist: {items.count()}")

            return render(request, 'wishlist/view_wishlist.html', {'wishlist': wishlist})
        else:
            logger.warning("Unauthenticated user attempted to access wishlist.")
            return redirect('login')
    except Exception as e:
        logger.error(f"Error viewing wishlist for user {request.user.id}: {str(e)}", exc_info=True)
        messages.error(request, "An error occurred while retrieving your wishlist.")
        return redirect('login')
    

def add_to_wishlist(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'Redirect', 'message': 'User not authenticated', 'redirect_url': reverse('login')}, status=401)

        try:
            data = json.loads(request.body)
            product_id = data['pid']

            product = get_object_or_404(products_hari, id=product_id)

            wishlist, created = Wishlist.objects.get_or_create(user=request.user, name='My Wishlist')
            if WishlistItem.objects.filter(wishlist=wishlist, product=product).exists():
                return JsonResponse({'status': 'Success', 'message': 'Product already in wishlist'}, status=200)
            else:
                WishlistItem.objects.create(wishlist=wishlist, product=product)
                return JsonResponse({'status': 'Success', 'message': 'Product added to wishlist'}, status=200)

        except products_hari.DoesNotExist:
            return JsonResponse({'status': 'Failed', 'message': 'Product does not exist'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'Failed', 'message': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'status': 'Failed', 'message': 'Invalid access'}, status=400)

@login_required
def remove_from_wishlist(request, item_id):
    try:
        item = get_object_or_404(WishlistItem, id=item_id, wishlist__user=request.user)
        item.delete()
        messages.success(request, "Item removed from wishlist.")
        logger.info(f"Item ID {item_id} removed from wishlist for user {request.user.id}.")
    except WishlistItem.DoesNotExist:
        messages.error(request, "Item not found in wishlist.")
        logger.error(f"Item ID {item_id} not found in wishlist for user {request.user.id}.")
    except Exception as e:
        messages.error(request, "An error occurred while trying to remove the item.")
        logger.error(f"Unexpected error removing item ID {item_id} from wishlist for user {request.user.id}: {str(e)}", exc_info=True)
    return redirect('view_wishlist')

def shared_wishlist(request, link):
    try:
        wishlist = get_object_or_404(Wishlist, shareable_link=link)
        owner = wishlist.user
        logger.info(f"Shared wishlist accessed by {request.user.id} with link: {link}.")
        return render(request, 'wishlist/shared_wishlist.html', {'wishlist': wishlist, 'owner': owner})
    except Exception as e:
        logger.error(f"Error accessing shared wishlist with link {link}: {str(e)}", exc_info=True)
        messages.error(request, "An error occurred while accessing the shared wishlist.")
        return redirect('home')


@login_required
def share_wishlist(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user, name='My Wishlist')
        shareable_link = wishlist.get_shareable_link()
        logger.info(f"User {request.user.id} generated a shareable link for their wishlist.")
        return JsonResponse({'status': 'Success', 'link': shareable_link}, status=200)
    except Wishlist.DoesNotExist:
        logger.error(f"Wishlist not found for user {request.user.id}.")
        return JsonResponse({'status': 'Failed', 'message': 'Wishlist not found'}, status=404)
    except Exception as e:
        logger.error(f"Unexpected error while sharing wishlist for user {request.user.id}: {str(e)}", exc_info=True)
        return JsonResponse({'status': 'Failed', 'message': 'An error occurred while sharing the wishlist.'}, status=500)




class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done') 

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')  


def password_reset_done(request):
    try:
        return render(request, 'registration/password_reset_done.html')
    except Exception as e:
        logger.error(f"Error rendering password reset done page: {str(e)}", exc_info=True)
        return render(request, 'registration/error.html', {'message': 'An error occurred while processing your request.'})

def password_reset_complete(request):
    try:
        return render(request, 'registration/password_reset_complete.html')
    except Exception as e:
        logger.error(f"Error rendering password reset complete page: {str(e)}", exc_info=True)
        return render(request, 'registration/error.html', {'message': 'An error occurred while processing your request.'})


def search(request):
    query = request.GET.get('q', '')
    products = []

    try:
        if query:
            products = products_hari.objects.filter(name__icontains=query).order_by('name') 
            
        logger.info("Search executed with query: %s", query)
        paginator = Paginator(products, 9) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'product/search_results.html', {'products': page_obj, 'query': query})

    except Exception as e:
        logger.error(f"Error during search: {str(e)}", exc_info=True)
        return render(request, 'product/search_results.html', {
            'products': [], 
            'query': query, 
            'error': 'An error occurred while searching. Please try again.'
        })



# def search_suggestions(request):
#     query = request.GET.get('q', '')
#     suggestions = []

#     try:
#         if query:
#             logger.info("searching starting")
#             products = products_hari.objects.filter(name__icontains=query)[:5] 
#             suggestions = [{'name': product.name, 'image': product.images.first().image.url} for product in products]

    
#     except Exception as e:
#         logger.error(f"Error fetching search suggestions: {str(e)}", exc_info=True)

#     return JsonResponse({'suggestions': suggestions})



@login_required
def change_password(request):
    try:
        if request.method == 'POST':
            form = CustomPasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user) 
                messages.success(request, 'Your password was successfully updated!')
                return redirect('Home')
        else:
            form = CustomPasswordChangeForm(request.user)
    except Exception as e:
        logger.error(f"Error occurred while changing password: {str(e)}", exc_info=True)
        messages.error(request, 'An error occurred while trying to update your password. Please try again.')

    return render(request, 'passwords/password_change.html', {'form': form})



def buy_now(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to buy products.")
        return JsonResponse({'status': 'Redirect', 'redirect_url': '/login'}, status=401)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('pid')
            product_qty = int(data.get('product_qty', 1))
            address = data.get('address')
            phone = data.get('phone')
            name = data.get('name')

            product = get_object_or_404(products_hari, id=product_id)

            if product.quantity < product_qty:
                logger.warning(f"Not enough stock for product {product_id}")
                return JsonResponse({'status': 'Not enough stock'}, status=400)

            order = Order.objects.create(
                user=request.user,
                total_price=product.selling_price * product_qty,
                name=name,
                address=address,
                phone=phone
            )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=product_qty,
                price=product.selling_price,
            )

            product.quantity -= product_qty
            product.save()

            logger.info(f"Order {order.id} placed successfully by {request.user.username}")

            return JsonResponse({'status': 'Success', 'redirect_url': f"/order_summary/{order.id}"}, status=200)

        except products_hari.DoesNotExist:
            logger.error(f"Product with id {product_id} does not exist")
            return JsonResponse({'status': 'Product does not exist'}, status=404)
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in the request body", exc_info=True)
            return JsonResponse({'status': 'Invalid data format'}, status=400)
        except Exception as e:
            logger.error(f"Error occurred during the buy_now process: {str(e)}", exc_info=True)
            return JsonResponse({'status': f'Error: {e}'}, status=500)
    
    logger.error("Invalid request method")
    return JsonResponse({'status': 'Invalid request'}, status=400)


def switch_user_form(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to switch users.")
        logger.warning("Unauthorized user tried to access switch user form.")
        return redirect('login')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user != request.user:
                login(request, user)
                messages.success(request, f"Switched to user: {user.username}")
                logger.info(f"User {request.user.username} switched to {user.username}")
                return redirect('Home')
            else:
                messages.error(request, "You are already logged in as this user.")
                logger.warning(f"User {request.user.username} attempted to switch to the same account.")
        else:
            messages.error(request, "Invalid username or password.")
            logger.error(f"Failed login attempt for username: {username}")

    return render(request, 'product/switch_user.html')

@login_required
def checkout(request):
    user_cart = cart_hari.objects.filter(user=request.user)

    if not user_cart.exists():
        messages.warning(request, "Your cart is empty")
        logger.warning(f"User {request.user.username} attempted to checkout with an empty cart.")
        return redirect('cart')

    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            total_price = sum(item.product.selling_price * item.product_qty for item in user_cart)
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']

            try:
                order = Order.objects.create(
                    user=request.user,
                    total_price=total_price,
                    name=name,
                    address=address,
                    phone=phone
                )
                
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

                # send_order_confirmation_email.delay(email, order.id)

                messages.success(request, "Order placed successfully")
                logger.info(f"Order {order.id} placed successfully by user {request.user.username}.")
                return redirect('order_summary', order_id=order.id)

            except Exception as e:
                logger.error(f"Error placing order for user {request.user.username}: {e}")
                messages.error(request, "There was an issue placing your order. Please try again.")
                return redirect('checkout')

    return render(request, 'checkout/checkout.html', {'form': form, 'cart': user_cart})


@login_required
def order_summary(request, order_id):
    try:

        order = get_object_or_404(Order, id=order_id, user=request.user)
        order_items = order.items.all()

        for item in order_items:
            item.price_per_item = item.price / item.quantity
            item.product_image = item.product.images.first() if item.product.images.exists() else None

        logger.info(f"Order summary accessed by user {request.user.username} for order {order.id}.")

        return render(request, 'checkout/order_summary.html', {'order': order, 'order_items': order_items})

    except Exception as e:
        logger.error(f"Error retrieving order summary for order {order_id} by user {request.user.username}: {e}")

        return render(request, 'error_page.html', {'message': 'Unable to retrieve order summary.'})

from django.utils.timezone import now


def home(request):
    try:

        logger.info("home view called")

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

        logger.info(f"All trending products are listed based on category successfully")


        # sale_products_query = products_hari.objects.filter(trending=False)
        # sale_products = []
        # logger.info(f"All sales products are listed successfully")
        # for product in sale_products_query:
        #     if product.sale_start_time:
        #         sale_end_time = product.sale_start_time + datetime.timedelta(hours=10)
        #         time_left = (sale_end_time - now()).total_seconds()

        #         if time_left > 0:
        #             sale_products.append({
        #                 'product': product,
        #                 'time_left': int(time_left),
        #             })
        # if sale_products:
        #     logger.info(f"All sales products are",sale_products)

        return render(request, 'shop/index.html', {
            "products": products,
            "mobiles": mobiles,
            "home": home,
            "fashion": fashion,
            "grocery": grocery,
            "electronics": electronics,
            # 'sale_products': sale_products,
            
        })
    
    except Exception as e:
        logger.error(f"Error in home view: {e}", exc_info=True)
        return render(request, 'shop/index.html', {
            "products": [],
            "mobiles": [],
            "home": [],
            "fashion": [],
            "grocery": [],
            "electronics": [],
            'sale_products':[],

        })


def user_page(request):
    try:
        logger.info("user_page view called")
        user = request.user
        id = user.id
        orders = Order.objects.filter(user=user).order_by('-created_at')
        logger.info(f"Number of orders for user {user.username}: {orders.count()}")

        return render(request, "shop/user.html", {'user': user, "id": id, "orders": orders})

    except Exception as e:
        logger.error(f"Error in user_page view: {e}", exc_info=True)
        return render(request, "shop/user.html", {'user': None, "id": None, "orders": []})


def cart_page(request):
    try:
        logger.info("cart_page view called")
        if request.user.is_authenticated:
            logger.info(f"Authenticated user: {request.user.username}")
            cart = cart_hari.objects.filter(user=request.user)
            for item in cart:
                item.product_image = item.product.images.first()

        else:
            logger.info("Unauthenticated user - using session-based cart")
            cart = request.session.get('cart', [])
            for item in cart:
                product = products_hari.objects.get(id=item['product_id'])
                item['product'] = product
                item['id'] = item['product_id'] 
                item['product_image'] = product.images.first()
                logger.info(f"Processing session cart item: {item['id']} for product {product.name}")
        return render(request, "product/cart.html", {'cart': cart})

    except Exception as e:
        logger.error(f"Error in cart_page view: {e}", exc_info=True)
        return render(request, "product/cart.html", {'cart': []})


def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            logger.info("AJAX request received for adding product to cart.")

            data = json.loads(request.body)
            product_id = data.get('pid')
            product_qty = data.get('product_qty')

            logger.info(f"Product ID: {product_id}, Quantity: {product_qty}")

            product_status = get_object_or_404(products_hari, id=product_id)
            logger.info(f"Product status retrieved: {product_status.name} (Stock: {product_status.quantity})")

            if request.user.is_authenticated:
                logger.info(f"Authenticated user: {request.user.username}")

                if cart_hari.objects.filter(user=request.user, product_id=product_id).exists():
                    logger.warning(f"Product {product_id} already in cart for user {request.user.username}")
                    messages.warning(request, "Item already in cart")
                    return JsonResponse({'status': 'Failed', 'message': 'Product already in cart'}, status=200)
                else:
                    if product_status.quantity >= product_qty:
                        cart_hari.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                        logger.info(f"Product {product_id} added to cart for user {request.user.username}")
                        messages.success(request, "Product added to cart")
                        return JsonResponse({'status': 'Success', 'message': 'Product added to cart'}, status=200)
                    else:
                        logger.warning(f"Insufficient stock for product {product_id} requested by user {request.user.username}")
                        messages.warning(request, "Product stock not available")
                        return JsonResponse({'status': 'Failed', 'message': 'Product stock not available'}, status=200)
            else:
                logger.info("Unauthenticated user - using session-based cart.")

                cart = request.session.get('cart', [])
                if any(item['product_id'] == product_id for item in cart):
                    logger.warning(f"Product {product_id} already in session cart.")
                    messages.warning(request, "Item already in cart")
                    return JsonResponse({'status': 'Failed', 'message': 'Product already in cart'}, status=200)

                if product_status.quantity >= product_qty:
                    cart.append({'product_id': product_id, 'product_qty': product_qty})
                    request.session['cart'] = cart
                    logger.info(f"Product {product_id} added to session cart.")
                    messages.success(request, "Product added to cart")
                    return JsonResponse({'status': 'Success', 'message': 'Product added to cart'}, status=200)
                else:
                    logger.warning(f"Insufficient stock for product {product_id} (session-based cart).")
                    messages.warning(request, "Product stock not available")
                    return JsonResponse({'status': 'Failed', 'message': 'Product stock not available'}, status=200)

        except json.JSONDecodeError:
            logger.error("JSON decoding error.",exc_info=True)
            messages.error(request, "Invalid data")
            return JsonResponse({'status': 'Failed', 'message': 'Invalid data'}, status=400)
    else:
        logger.error("Invalid access - non-AJAX request made.",exc_info=True)
        messages.error(request, "Invalid access",)
        return JsonResponse({'status': 'Failed', 'message': 'Invalid access'}, status=400)

def remove_cart(request, uid):
    if request.user.is_authenticated:
        try:
            logger.info(f"Authenticated user {request.user.username} attempting to remove item {uid} from cart.")
            
            cartitem = cart_hari.objects.get(id=uid, user=request.user)
            cartitem.delete()
            
            logger.info(f"Item {uid} removed from cart for user {request.user.username}.")
            messages.success(request, "Item removed from cart")
            
        except cart_hari.DoesNotExist:
            logger.warning(f"Item {uid} not found in the cart for user {request.user.username}.", exc_info=True)
            messages.error(request, "Item not found in your cart")
            
        except cart_hari.MultipleObjectsReturned:
            logger.error(f"Multiple items found with ID {uid} for user {request.user.username}.", exc_info=True)
            messages.error(request, "Multiple items found with the same ID, please contact support")
    
    else:
        logger.info("Unauthenticated user attempting to remove item from session-based cart.")
        
        try:
            cart = request.session.get('cart', [])
            updated_cart = [item for item in cart if item['product_id'] != uid]
            
            if len(updated_cart) < len(cart):
                request.session['cart'] = updated_cart
                logger.info(f"Item {uid} removed from session-based cart.")
                messages.success(request, "Item removed from cart")
            else:
                logger.warning(f"Item {uid} not found in session-based cart.")
                messages.error(request, "Item not found in your cart")
        
        except Exception as e:
            logger.error(f"An error occurred while removing item {uid} from session-based cart.", exc_info=True)
            messages.error(request, "An error occurred while processing your request. Please try again.")
    
    return redirect("cart")


def fav_view(request):
    if request.user.is_authenticated:
        logger.info(f"Authenticated user {request.user.username} is viewing their favorites.")
        try:
            fav = favourite_hari.objects.filter(user=request.user)
            for item in fav:
                item.product_image = item.product.images.first()
            logger.info(f"Successfully retrieved {len(fav)} favorite items for user {request.user.username}.")
        except Exception as e:
            logger.error(f"Error retrieving favorite items for user {request.user.username}.", exc_info=True)
            fav = []
            logger.warning(f"Defaulting to empty favorites list for user {request.user.username}.")
    
    else:
        logger.info("Unauthenticated user is viewing session-based favorites.")
        try:
            fav = request.session.get('favourites', [])
            for item in fav:
                product = products_hari.objects.get(id=item['product_id'])
                item['product'] = product
                item['id'] = item['product_id'] 
                item['product_image'] = product.images.first()
            logger.info(f"Successfully retrieved {len(fav)} favorite items from session for unauthenticated user.")
        except products_hari.DoesNotExist:
            logger.error(f"Product not found in session-based favorites.", exc_info=True)
            fav = []
            logger.warning("Defaulting to empty favorites list for session-based user.")
        except Exception as e:
            logger.error("Error retrieving session-based favorites.", exc_info=True)
            fav = []
            logger.warning("Defaulting to empty favorites list for session-based user.")

    return render(request, "product/favourite.html", {'fav': fav})


def fav_page(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            data = json.loads(request.body)
            product_id = data['pid']
            
            logger.info(f"Received request to add product {product_id} to favourites via AJAX.")
            
            product_status = products_hari.objects.get(id=product_id)
            
            if product_status:
                if request.user.is_authenticated:
                    logger.info(f"Authenticated user {request.user.username} trying to add product {product_id} to favourites.")
                    
                    if favourite_hari.objects.filter(user=request.user.id, product_id=product_id).exists():
                        messages.success(request, "Product already in favourites")
                        logger.info(f"Product {product_id} already in favourites for user {request.user.username}.")
                        return JsonResponse({'status': 'Success'}, status=200)
                    else:
                        favourite_hari.objects.create(user=request.user, product_id=product_id)
                        messages.success(request, "Product added to favourites")
                        logger.info(f"Product {product_id} successfully added to favourites for user {request.user.username}.")
                        return JsonResponse({'status': 'Success'}, status=200)
                else:
                    logger.info("Unauthenticated user adding product to session-based favourites.")
                    favourites = request.session.get('favourites', [])
                    for item in favourites:
                        if item['product_id'] == product_id:
                            messages.success(request, "Product already in favourites")
                            logger.info(f"Product {product_id} already in session-based favourites.")
                            return JsonResponse({'status': 'Success'}, status=200)
                    
                    favourites.append({'product_id': product_id})
                    request.session['favourites'] = favourites
                    messages.success(request, "Product added to favourites")
                    logger.info(f"Product {product_id} successfully added to session-based favourites.")
                    return JsonResponse({'status': 'Success'}, status=200)

        except products_hari.DoesNotExist:
            messages.error(request, "Product does not exist")
            logger.error(f"Product with ID {product_id} does not exist.", exc_info=True)
            return JsonResponse({'status': 'Failed'}, status=404)
        except json.JSONDecodeError:
            messages.error(request, "Invalid data")
            logger.error("JSON decoding error in request body.", exc_info=True)
            return JsonResponse({'status': 'Failed'}, status=400)
        except Exception as e:
            logger.error("An unexpected error occurred.", exc_info=True)
            messages.error(request, "An error occurred while processing your request.")
            return JsonResponse({'status': 'Failed'}, status=500)
    else:
        messages.error(request, "Invalid access")
        logger.warning("Invalid access attempt to fav_page.")
        return JsonResponse({'status': 'Failed'}, status=400)


def remove_fav(request, fid):
    if request.user.is_authenticated:
        try:
            logger.info(f"Authenticated user {request.user.username} attempting to remove item {fid} from favourites.")
            favitem = favourite_hari.objects.get(id=fid, user=request.user)
            favitem.delete()
            messages.success(request, "Item removed from favourites")
            logger.info(f"Item {fid} successfully removed from favourites for user {request.user.username}.")
        except favourite_hari.DoesNotExist:
            messages.error(request, "Item not found in your favourites")
            logger.error(f"Item {fid} not found in favourites for user {request.user.username}.", exc_info=True)
        except favourite_hari.MultipleObjectsReturned:
            messages.error(request, "Multiple items found with the same ID, please contact support")
            logger.error(f"Multiple items found with ID {fid} for user {request.user.username}.", exc_info=True)
    else:
        logger.info("Unauthenticated user attempting to remove item from session-based favourites.")
        favourites = request.session.get('favourites', [])
        
        try:
            updated_favourites = [item for item in favourites if item['product_id'] != fid]
            
            if len(updated_favourites) < len(favourites):
                request.session['favourites'] = updated_favourites
                messages.success(request, "Item removed from favourites")
                logger.info(f"Item {fid} successfully removed from session-based favourites.")
            else:
                messages.error(request, "Item not found in your favourites")
                logger.error(f"Item {fid} not found in session-based favourites.")
        except Exception as e:
            messages.error(request, "An error occurred while processing your request.")
            logger.error(f"Error while removing item {fid} from session-based favourites: {str(e)}", exc_info=True)

    return redirect("fav_view")

def logout_page(request):
    if request.user.is_authenticated:
        try:
            logger.info(f"User {request.user.username} is attempting to log out.")
            logout(request)
            messages.success(request, "Logged Out Successfully")
            logger.info(f"User {request.user.username} logged out successfully.")
        except Exception as e:
            messages.error(request, "An error occurred while logging out. Please try again.")
            logger.error(f"Error while logging out user {request.user.username}: {str(e)}", exc_info=True)
    else:
        logger.warning("Unauthenticated user attempted to log out.")
        
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
            logger.info(f"User {name} logged in successfully.")

            session_cart = request.session.get('cart', [])
            for item in session_cart:
                product_id = item['product_id']
                product_qty = item['product_qty']
                try:
                    if not cart_hari.objects.filter(user=request.user, product_id=product_id).exists():
                        cart_hari.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                except Exception as e:
                    logger.error(f"Error adding product ID {product_id} to cart for user {name}: {str(e)}", exc_info=True)

            session_favourites = request.session.get('favourites', [])
            for item in session_favourites:
                product_id = item['product_id']
                try:
                    if not favourite_hari.objects.filter(user=request.user, product_id=product_id).exists():
                        favourite_hari.objects.create(user=request.user, product_id=product_id)
                except Exception as e:
                    logger.error(f"Error adding product ID {product_id} to favourites for user {name}: {str(e)}", exc_info=True)

            request.session['favourites'] = []
            request.session['cart'] = []

            return redirect(next_url)
        else:
            messages.error(request, "Invalid User Name or password")
            logger.warning(f"Failed login attempt for user {name}.")
            return redirect(f"/login?next={next_url}")
    
    return render(request, 'product/login.html', {'next': next_url})

def register(request):
    next_url = request.GET.get('next', '/')
    form = CustomuserForm()
    
    if request.method == "POST":
        form = CustomuserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.last_login = timezone.now()
                user.save()
                messages.success(request, "Registration Successful. You Can Login now")
                logger.info(f"User {user.username} registered successfully.")
                return redirect(f"/login?next={next_url}")
            except Exception as e:
                messages.error(request, "An error occurred during registration. Please try again.")
                logger.error(f"Error during registration: {str(e)}", exc_info=True)

    return render(request, 'shop/register.html', {'form': form})

def collectionview(request, name):
    try:
        if category_hari.objects.filter(status=0, name=name).exists():
            products = products_hari.objects.filter(category__name=name)
            logger.info(f"Products retrieved for category '{name}': {products.count()} items found.")
            return render(request, 'product/index.html', {'products': products, 'category': name})
        else:
            messages.warning(request, "No such Category found!!!")
            logger.warning(f"Category '{name}' not found in the database.")
            return redirect('Collection')
    except Exception as e:
        logger.error(f"Error retrieving products for category '{name}': {str(e)}", exc_info=True)
        messages.error(request, "An error occurred while retrieving the category.")
        return redirect('Collection')


def product_details(request, cname, pname):
    try:
        if category_hari.objects.filter(status=0, name=cname).exists():

            product = products_hari.objects.filter(status=0, name=pname).first()
            if product:
                logger.info(f"Product details retrieved for '{pname}' in category '{cname}'.")
                return render(request, "product/product_details.html", {"products": product})
            else:
                messages.warning(request, "No such Product found!!!")
                logger.warning(f"Product '{pname}' not found in category '{cname}'.")
                return redirect('Collection')
        else:
            messages.error(request, "No such Category found!!!")
            logger.error(f"Category '{cname}' not found.")
            return redirect('Collection')
    except Exception as e:
        logger.error(f"Error retrieving product details for '{pname}' in category '{cname}': {str(e)}", exc_info=True)
        messages.error(request, "An error occurred while retrieving the product details.")
        return redirect('Collection')