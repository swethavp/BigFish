from django.urls import path
from .import views

urlpatterns=[
    path('fishindex/',views.fishindex,name='fishindex'),
    path('products/<str:cat>',views.products,name='products'),
    path('recipe/',views.recipe,name='recipe'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('contactdata/',views.contactdata,name='contactdata'),
    path('single_product/<int:dataid>',views.single_product,name='single_product'),
    path('single_recipe/<int:dataid>',views.single_recipe,name='single_recipe'),
    path('login/',views.login,name='login'),
    path('logindata/',views.logindata,name='logindata'),
    path('register/',views.register,name='register'),
    path('registerdata/',views.registerdata,name='registerdata'),
    path('cart/<int:prodid>',views.cart,name='cart'),
    path('cart1/',views.cart1,name='cart1'),
    path('checkout/',views.checkout,name='checkout'),
    path('cartupdate/',views.cartupdate,name='cartupdate'),
    path('deletecart/<int:dataid>',views.deletecart,name='deletecart'),
    path('orderdata/',views.orderdata,name='orderdata'),
    path('logout/',views.logout,name='logout')
]