from django.shortcuts import render,redirect
from bigfishapp.models import admindb
from django.http import HttpResponse,JsonResponse
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from bigfishapp.models import categorydb
from bigfishapp.models import productdb
from bigfishapp.models import recipedb 
from fishapp.models import contactdb,registerdb,Cart,order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):

    user=registerdb.objects.all().count()
    c=Cart.objects.all().count()
    o=order.objects.all().count()
    m=contactdb.objects.all().count()
    return render(request,'index.html',{'user':user,'c':c,'o':o,'m':m})

def adlogin(request):
    
    return render(request,'adminlogin.html')

def admin_login(request):
    username_r = request.POST.get("username")
    password_r = request.POST.get("password")
    print(password_r)
    print(username_r)
    if User.objects.filter(username__contains=username_r).exists():
        user = authenticate(username =username_r, password=password_r)
        if user is not None:
            login(request,user)
            request.session['username']=username_r
            request.session['password']=password_r
            print(user)
            return redirect('index')
        else:
            return render(request,'adminlogin.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return redirect('adlogin')


def adminlogout(request):

    del request.session['username']
    del request.session['password']
    return redirect('adlogin')

def addadmin(request):
    return render(request,'addadmin.html')
def admindata(request):
    if request.method == "POST":
        name_r=request.POST.get('name')
        email_r=request.POST.get('email')
        password_r=request.POST.get('password')
        mobile_r=request.POST.get('mobile')
        file_r=request.FILES['file']
        
        obj=admindb(Name=name_r,Email=email_r,Password=password_r,Mobile=mobile_r,FileUpload=file_r)
        obj.save()
        
        return redirect('addadmin')

def viewadmin(request):
    if 'username' in request.session.keys():
        data=admindb.objects.all()
        return render(request,'viewadmin.html',{'data':data})

def editadmin(request,dataid):
    if 'username' in request.session.keys():
        data=admindb.objects.filter(id=dataid)
        return render(request,'editadmin.html',{'data':data})

def updateadmin(request,dataid):
    if request.method == "POST":
        name_r=request.POST.get('name')
        email_r=request.POST.get('email')
        password_r=request.POST.get('password')
        mobile_r=request.POST.get('mobile')
        try:
            file_r=request.FILES['file']
            fs = FileSystemStorage() 
            file = fs.save(file_r.name, file_r)
        except MultiValueDictKeyError :
            file=admindb.objects.get(id=dataid).file
        admindb.objects.filter(id=dataid).update(Name=name_r,Email=email_r,Password=password_r,Mobile=mobile_r,FileUpload=file_r)
       
        return redirect('viewadmin')

def deleteadmin(request,dataid):
    if request.method == "POST":
        name_r=request.POST.get('name')
        email_r=request.POST.get('email')
        password_r=request.POST.get('password')
        mobile_r=request.POST.get('mobile')
        
        admindb.objects.filter(id=dataid).delete()
       
        return redirect('viewadmin')

def addcategory(request):
    if 'username' in request.session.keys():
        return render(request,'addcategory.html')

def categorydata(request):
    data=dict()
    if request.method == "POST":
        cname_r=request.POST.get('catname')
        if categorydb.objects.filter(Category_name=cname_r).exists():
            data['error']=0
            data['message']="This category already exist"
            return JsonResponse(data)
        cdesc_r=request.POST.get('cdesc')
        img_r=request.FILES['img']
        obj=categorydb(Category_name=cname_r,Category_description=cdesc_r,FileUpload=img_r)
        obj.save()
        
        return redirect('addcategory')


def viewcategory(request):
    if 'username' in request.session.keys():
        data=categorydb.objects.all()
        return render(request,'viewcategory.html',{'data':data})


def editcat(request,dataid):
    if 'username' in request.session.keys():
        data=categorydb.objects.filter(id=dataid)
        return render(request,'editcat.html',{'data':data})

def updatecat(request,dataid):
    if request.method == "POST":
        cname_r=request.POST.get('catname')
        cdesc_r=request.POST.get('cdesc')
        try:
            img_r=request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img_r.name, img_r)
        except MultiValueDictKeyError :
            file=categorydb.objects.get(id=dataid).FileUpload
        categorydb.objects.filter(id=dataid).update(Category_name=cname_r,Category_description=cdesc_r,FileUpload=file)
       
        return redirect('viewcategory')

def deletecat(request,dataid):
    if request.method == "POST":
        cname_r=request.POST.get('catname')
        cdesc_r=request.POST.get('cdesc')

        categorydb.objects.filter(id=dataid).delete()
       
        return redirect('viewcategory')

def addproduct(request):
    if 'username' in request.session.keys():
        da=categorydb.objects.all()
        return render(request,'addproduct.html',{'da':da})

def productdata(request):
    data=dict()
    if request.method == "POST":
        pname_r=request.POST.get('pname')
        if productdb.objects.filter(Product_Name=pname_r).exists():
            data['error']=0
            data['message']="This product already exist"
            return JsonResponse(data)
        pweight_r=request.POST.get('pweight')
        price_r=request.POST.get('price')
        pcat_r=request.POST.get('pcat')
        pfile_r=request.FILES['pfile']
        
        obj=productdb(Product_Name=pname_r,Product_Weight=pweight_r,Product_Price=price_r,Product_Category=pcat_r,Image=pfile_r)
        obj.save()
        
        return redirect('addproduct')



def viewproduct(request):
    if 'username' in request.session.keys():
        data=productdb.objects.all()
        return render(request,'viewproduct.html',{'data':data})


def editpro(request,dataid):
    if 'username' in request.session.keys():
        data=productdb.objects.filter(id=dataid)
        return render(request,'editpro.html',{'data':data})

def updatepro(request,dataid):
    if request.method == "POST":
        pname_r=request.POST.get('pname')
        pweight_r=request.POST.get('pweight')
        price_r=request.POST.get('price')
        pcat_r=request.POST.get('pcat')
        
        
        try:
            pfile_r=request.FILES['pfile']
            fs = FileSystemStorage() 
            file = fs.save(pfile_r.name, pfile_r)
        except MultiValueDictKeyError :
            file=productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Product_Name=pname_r,Product_Weight=pweight_r,Product_Price=price_r,Product_Category=pcat_r,Image=file)
       
        return redirect('viewproduct')

def deletepro(request,dataid):
    if request.method == "POST":
        pname_r=request.POST.get('pname')
        pweight_r=request.POST.get('pweight')
        price_r=request.POST.get('price')
        pcat_r=request.POST.get('pcat')
    
        productdb.objects.filter(id=dataid).delete()
       
        return redirect('viewproduct')

def addrecipe(request):
    if 'username' in request.session.keys():
        return render(request,'addrecipe.html')

def recipedata(request):
    data=dict()
    if request.method == "POST":
        rname_r=request.POST.get('rname')
        if recipedb.objects.filter(Recipe_Name=rname_r).exists():
            data['error']=0
            data['message']="This recipe already exist"
            return JsonResponse(data)
        ringredients_r=request.POST.get('ringredients')
        rinstructions_r=request.POST.get('rinstructions')
        rfile_r=request.FILES['rfile']
        
        obj=recipedb(Recipe_Name=rname_r,Recipe_Ingredients=ringredients_r,Recipe_Instructions=rinstructions_r,Recipe_Image=rfile_r)
        obj.save()
        
        return redirect('addrecipe')

def viewrecipe(request):
    if 'username' in request.session.keys():
        data=recipedb.objects.all()
        return render(request,'viewrecipe.html',{'data':data})


def editrec(request,dataid):
    if 'username' in request.session.keys():
        data=recipedb.objects.filter(id=dataid)
        return render(request,'editrec.html',{'data':data})

def updaterec(request,dataid):
    if request.method == "POST":
       rname_r=request.POST.get('rname')
       ringredients_r=request.POST.get('ringredients')
       rinstructions_r=request.POST.get('rinstructions')
       try:
            rfile_r=request.FILES['rfile']
            fs = FileSystemStorage() 
            file = fs.save(rfile_r.name, rfile_r)
       except MultiValueDictKeyError :
            file=recipedb.objects.get(id=dataid).Recipe_Image
       recipedb.objects.filter(id=dataid).update(Recipe_Name=rname_r,Recipe_Ingredients=ringredients_r,Recipe_Instructions=rinstructions_r,Recipe_Image=file)
       return redirect('viewrecipe')

def deleterec(request,dataid):
    if request.method == "POST":
        rname_r=request.POST.get('rname')
        ringredients_r=request.POST.get('ringredients')
        rinstructions_r=request.POST.get('rinstructions')
        
        recipedb.objects.filter(id=dataid).delete()
       
        return redirect('viewrecipe')

def message(request):
    if 'username' in request.session.keys():
        # data=productdb.objects.all()
        data=contactdb.objects.all()
        return render(request,'message.html',{'data':data})

def reguser(request):
    if 'username' in request.session.keys():
        data=registerdb.objects.all()
        return render(request,'reguser.html',{'data':data})

def orders(request):
    if 'username' in request.session.keys():
        data=order.objects.all()
        return render(request,'orders.html',{'data':data})
    
def viewcart(request):
    if 'username' in request.session.keys():
        data=Cart.objects.all()
        return render(request,'viewcart.html',{'data':data})
