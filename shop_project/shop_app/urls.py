from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="Home"),
    path('user/',views.user_page,name="user"),
    path('register',views.register,name="Register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('collections',views.collections,name="Collections"),
    path('collection/<str:name>/', views.collectionview, name='collection'),
    path('collection/<str:cname>/<str:pname>', views.product_details, name='product_details'),
    path('addtocart/',views.add_to_cart,name="addtocart"),
    path('cart/',views.cart_page,name="cart"),
    path('remove_cart/<str:uid>',views.remove_cart,name="remove_cart"),
    path('fav/',views.fav_page,name="fav"),
    path('fav_view/',views.fav_view,name="fav_view"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('checkout/', views.checkout, name='checkout'),
    path('order_summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('switch_user/', views.switch_user_form, name='switch_user_form'),
    path('buy_now/', views.buy_now, name='buy_now'),
]