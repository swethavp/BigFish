from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from bigfishapp.models import categorydb
from bigfishapp.models import productdb
from bigfishapp.models import recipedb
from fishapp.models import contactdb,registerdb,Cart,order
from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def fishindex(request):
    data=categorydb.objects.all()
    da=productdb.objects.all()
    return render(request,'fishindex.html',{'data':data,'da':da})

def products(request,cat):
    # data=productdb.objects.all()
    print(cat)
    if (cat=="all"):
        data=productdb.objects.all()
    else:
        data=productdb.objects.filter(Product_Category=cat)
    return render(request,'products.html',{'data':data})

def recipe(request):
    data=recipedb.objects.all()
    return render(request,'recipe.html',{'data':data})

    
def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def contactdata(request):
    if request.method == "POST":
        name_r=request.POST.get('name')
        email_r=request.POST.get('email')
        subject_r=request.POST.get('subject')
        message_r=request.POST.get('message')
        
        obj=contactdb(Name=name_r,Email=email_r,Subject=subject_r,Message=message_r)
        obj.save()
        
        return redirect('contact')

def single_product(request,dataid):
    data=productdb.objects.filter(id=dataid)
    return render(request,'single_product.html',{'data':data})

def single_recipe(request,dataid):
    data=recipedb.objects.filter(id=dataid)
    return render(request,'single_recipe.html',{'data':data})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def registerdata(request):
    if request.method == "POST":
        name_r=request.POST.get('name')
        email_r=request.POST.get('email')
        address_r=request.POST.get('address')
        phone_r=request.POST.get('phone')
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')

        obj=registerdb(Name=name_r,Email=email_r,Address=address_r,PhoneNo=phone_r,Username=username_r,Password=password_r)
        obj.save()
        
        return redirect('login')

def logindata(request):
    if request.method == 'POST':
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if registerdb.objects.filter(Username=username_r,Password=password_r).exists():
            data=registerdb.objects.filter(Username=username_r,Password=password_r).values('Name','Email','PhoneNo','id').first()
            request.session['username']=username_r
            request.session['password']=password_r
            request.session['email']=data['Email']
            request.session['phone']=data['PhoneNo']
            request.session['id']=data['id']
            return redirect("fishindex")
        else:
            return render(request,'login.html',{'msg':"Sorry... Invalid username or password"})

def logout(request):
    del request.session['username']
    del request.session['password']
    #del request.session['email']
    #del request.session['phone']
    #del request.session['id']
    return redirect("fishindex")

def cart(request,prodid):
    if 'id' in request.session.keys():
        if Cart.objects.filter(productid=prodid,status=0,userid=request.session.get('id')).exists():
            quantity=request.POST.get('quantity')
            total=request.POST.get('total')
            userid=request.POST.get('userid')
            username=request.POST.get('username')
            Cart.objects.filter(productid=prodid,status=0).update(Total=total,quantity=quantity)
            return redirect('cart1')
        else:
            quantity=request.POST.get('quantity')
            total=request.POST.get('total')
            userid=request.POST.get('userid')
            username=request.POST.get('username')
            print("***********************************************")
            print(userid)
            obj=Cart(productid=productdb.objects.get(id=prodid),Total=total,quantity=quantity,userid=registerdb.objects.get(id=userid),status=0)
            obj.save()
            return redirect('cart1')
    else:
        return redirect('fishindex')

def cart1(request):
    #data=Cart.objects.all()
    co=request.session.get('id')
    data=Cart.objects.filter(userid=co,status=0)
    subtotal=Cart.objects.filter(userid=co,status=0).aggregate(Sum('Total'))
    s=subtotal['Total__sum']
    return render(request,'cart.html',{'data':data, 's':s})

    
@csrf_exempt
def cartupdate(request):
    if request.method == 'POST':
        cartid=request.POST.get('pid')
        q=request.POST.get('quantity')
        p=request.POST.get('price')
        T=int(q)*int(p)
        Cart.objects.filter(id=cartid).update(quantity=q,Total=T)
        return HttpResponse()

def deletecart(request,dataid):
    if request.method == "POST":
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        total=request.POST.get('total')
        Cart.objects.filter(id=dataid).delete()
       
        return redirect('cart1')


def checkout(request):
    co=request.session.get('id')
    data=Cart.objects.filter(userid=co,status=0)
    subtotal=Cart.objects.filter(userid=co,status=0).aggregate(Sum('Total'))
    s=subtotal['Total__sum']
    return render(request,'checkout.html',{'data':data, 's':s})
  
def orderdata(request):
    if request.method == "POST":
        fname_r=request.POST.get('fname')
        lname_r=request.POST.get('lname')
        dist_r=request.POST.get('dist')
        print(dist_r)
        street_r=request.POST.get('street')
        appartment_r=request.POST.get('appartment')
        town_r=request.POST.get('town')
        pin_r=request.POST.get('pin')
        phone_r=request.POST.get('phone')
        email_r=request.POST.get('email')
        userid=request.session.get('id')
        print(userid)
        data=Cart.objects.filter(userid=userid,status=0)
        print(data)
        for a in data:
            obj=order(cartid=Cart.objects.get(id=a.id),firstname=fname_r,lastname=lname_r,district=dist_r,street_address=street_r,appartment=appartment_r,town=town_r,pin=pin_r,phone=phone_r,email=email_r)
            obj.save()
            Cart.objects.filter(id=a.id).update(status=1)
        return redirect('fishindex')