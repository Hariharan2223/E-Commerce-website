from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomPasswordResetView, CustomPasswordResetConfirmView, password_reset_done, password_reset_complete

urlpatterns=[
    path('',views.home,name="Home"),
    path('user/',views.user_page,name="user"),
    path('switch_user/', views.switch_user_form, name='switch_user_form'),

    # Authentication
    path('register',views.register,name="Register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),

    # collection
    path('collections',views.collections,name="Collections"),
    path('collection/<str:name>/', views.collectionview, name='collection'),
    path('collection/<str:cname>/<str:pname>', views.product_details, name='product_details'),

    # cart
    path('addtocart/',views.add_to_cart,name="addtocart"),
    path('cart/',views.cart_page,name="cart"),
    path('remove_cart/<str:uid>',views.remove_cart,name="remove_cart"),

    # favourite
    path('fav/',views.fav_page,name="fav"),
    path('fav_view/',views.fav_view,name="fav_view"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),

    # buy_product
    path('buy_now/', views.buy_now, name='buy_now'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_summary/<int:order_id>/', views.order_summary, name='order_summary'), 
    
    # search_feature
    path('search/', views.search, name='search'),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),

    # password
    path('change_password/', views.change_password, name='change_password'),
    path('reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', password_reset_done, name='password_reset_done'),
    path('reset/complete/', password_reset_complete, name='password_reset_complete'),

    # # wishlist
    path('wishlist/share/', views.share_wishlist, name='share_wishlist'),
    path('addtowishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/share/<uuid:link>/', views.shared_wishlist, name='shared_wishlist'),

    
    


]