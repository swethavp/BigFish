from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns=[
    path('',views.adlogin,name='adlogin'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('index/',views.index,name='index'),
    path('addadmin/',views.addadmin,name='addadmin'),
    path('admindata/',views.admindata,name='admindata'),
    path('viewadmin/',views.viewadmin,name='viewadmin'),
    path('editadmin/<int:dataid>',views.editadmin,name='editadmin'), 
    path('updateadmin/<int:dataid>',views.updateadmin,name='updateadmin'), 
    path('deleteadmin/<int:dataid>',views.deleteadmin,name='deleteadmin'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('categorydata/',views.categorydata,name='categorydata'),
    path('viewcategory/',views.viewcategory,name='viewcategory'),
    path('editcat/<int:dataid>',views.editcat,name='editcat'), 
    path('updatecat/<int:dataid>',views.updatecat,name='updatecat'),
    path('deletecat/<int:dataid>',views.deletecat,name='deletecat'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('productdata/',views.productdata,name='productdata'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('editpro/<int:dataid>',views.editpro,name='editpro'), 
    path('updatepro/<int:dataid>',views.updatepro,name='updatepro'),
    path('deletepro/<int:dataid>',views.deletepro,name='deletepro'),
    path('addrecipe/',views.addrecipe,name='addrecipe'),
    path('recipedata/',views.recipedata,name='recipedata'),
    path('viewrecipe/',views.viewrecipe,name='viewrecipe'),
    path('editrec/<int:dataid>',views.editrec,name='editrec'), 
    path('updaterec/<int:dataid>',views.updaterec,name='updaterec'),
    path('deleterec/<int:dataid>',views.deleterec,name='deleterec'),
    path('message/',views.message,name='message'),
    path('reguser/',views.reguser,name='reguser'),
    path('orders/',views.orders,name='orders'),
    path('viewcart/',views.viewcart,name='viewcart'),
    path('adminlogout/',views.adminlogout,name='adminlogout')
    
]