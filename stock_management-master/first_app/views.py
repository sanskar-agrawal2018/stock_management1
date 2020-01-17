from django.shortcuts import render,redirect
from . import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from first_app.forms import RegisterUserForm,Loginform,BookEnterForm,Storeform,ElectronicEnterForm,SportEnterForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from  django.contrib import messages

# Create your views here.

def usercreate(request):
    form=RegisterUserForm()
    form1=Loginform()
    if request.method=='POST':
        form=RegisterUserForm(request.POST)
        form1=Loginform(request.POST)
    if (form.is_valid() and form1.is_valid()):
        user=form1.save()
        user.set_password(user.password)
        user.save()
        obj=models.User1()
        login_id12 = form1.cleaned_data['username']
        messages.success(request,f'Account created for {login_id12}')
        obj.login_id=User.objects.filter(username=login_id12)[0]
        obj.f_name=form.cleaned_data['f_name']
        obj.m_name = form.cleaned_data['m_name']
        obj.l_name=form.cleaned_data['l_name']
        obj.Hostel_Type=form.cleaned_data['Hostel_Type']
        obj.Block=form.cleaned_data['Block']
        obj.Email_Id=form.cleaned_data['Email_Id']
        obj.DOB=form.cleaned_data['DOB']
        obj.save()
        return index(request)
    else:
        print("Error")
    return render(request,'first_app/register.html',{'form':form,'form1':form1})





def StoreEnter(request):
    form=Storeform()
    if request.method=='POST':
        form=Storeform(request.POST)
    if (form.is_valid()):
        form.save(commit=True)
    return render(request,'first_app/storeEnter.html',{"form":form})

def basic(request):
    return render(request,'first_app/basic.html')

def index(request):
    return render(request,'first_app/index.html')

class BookListView(ListView):
    model=models.Books

    def get_queryset(self,*args,**kargs):
        qs=super(BookListView,self).get_queryset(*args,**kargs)
        qs=qs.filter(sold=False)
        # print("1 Yes")
        return qs

class BookDetail(DetailView):
    model=models.Books



class BookBuy(DetailView):
    template_name = 'first_app/book_buy.html'
    model=models.Books

@login_required
def bookBuyConfirmed(request,pk):
    temp=models.Books.objects.filter(Book_Id=pk)[0]
    temp.sold=True
    print(temp.user_id)
    user_id=models.User.objects.filter(username=temp.user_id)[0]
    user = models.User1.objects.filter(login_id=user_id.id)[0]
    # print(user)
    param={'book_name':temp.Book_Name,'book_descrition':temp.Descrition,'book_price':temp.Book_Price,'book_edition':temp.Edition,'book_publication':temp.Publisher,'user_name':user.f_name,'user_middle_name':user.m_name,'user_last_name':user.l_name,'user_Hostel_Type':user.Hostel_Type,'user_Block':user.Block,"user_Email_ID":user.Email_Id}
    temp.save()
    basket=models.Shopping_Basket()
    basket.user_id=user_id
    basket.books=temp
    basket.save()
    return render(request,'first_app/book_buy.html',param)
#
# def user_login(request,next):
#     print("Come")
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         print("Authicate")
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 print("Yes")
#                 return HttpResponseRedirect('/first_app'+'/'+next)
#             else:
#                 print("Not found")
#         else:
#             return HttpResponseRedirect('/first_app/login')
#     else:
#         return render(request,'first_app/login.html')

@login_required
def bookEnter(request):
    form=BookEnterForm()
    if request.method=='POST':
        form=BookEnterForm(request.POST)
    if (form.is_valid()):
        # form.save()
        # Book_Name = form.cleaned_data['Book_Name']
        # obj=models.Books.objects.filter(Book_Name=Book_Name)[0]
        obj=models.Books()
        obj.Course_Id=form.cleaned_data['Course_Id']
        obj.Book_Name=form.cleaned_data['Book_Name']
        obj.Book_Price=form.cleaned_data['Book_Price']
        obj.Publisher=form.cleaned_data['Publisher']
        obj.Edition=form.cleaned_data['Edition']
        obj.Descrition=form.cleaned_data['Descrition']
        obj.user_id=request.user
        # obj.store_id = 'No store'
        obj.save()
        # obj.sold=False
        # obj.of_shop=False
        # obj.quantity=1

        # print(obj.Course_Id)
        # print(User.is_authenticated,User.is_active,User.first_name,request.user)
        return redirect('/first_app/bookview')
    return render(request,'first_app/bookEnter.html',{"form":form,'title':"Books"})

@login_required
def sportEnter(request):
    # print("I  m in electronic enter")
    # print("I  m in electronic enter")
    form=SportEnterForm()
    # print(form)
    if request.method=='POST':
        form=SportEnterForm(request.POST)
    if (form.is_valid()):
        # form.save()
        # Book_Name = form.cleaned_data['Book_Name']
        # obj=models.Books.objects.filter(Book_Name=Book_Name)[0]
        obj=models.Sports()
        # obj.=form.cleaned_data['garantee']
        obj.item_name=form.cleaned_data['item_name']
        obj.item_price=form.cleaned_data['item_price']
        obj.descrition_text=form.cleaned_data['descrition_text']
        # obj.product_models=form.cleaned_data['product_models']
        # obj.description_text=form.cleaned_data['description_text']
        obj.user_id=request.user
        # obj.store_id = 'No store'
        obj.save()
        # obj.sold=False
        # obj.of_shop=False
        # obj.quantity=1

        # print(obj.Course_Id)
        # print(User.is_authenticated,User.is_active,User.first_name,request.user)
        return redirect('/first_app/sportview')


    return render(request,'first_app/bookEnter.html',{"form":form,'title':"Sports Item"})


@login_required
def electronicEnter(request):
    # print("I  m in electronic enter")
    # print("I  m in electronic enter")
    form=ElectronicEnterForm()
    # print(form)
    if request.method=='POST':
        form=ElectronicEnterForm(request.POST)
    if (form.is_valid()):
        # form.save()
        # Book_Name = form.cleaned_data['Book_Name']
        # obj=models.Books.objects.filter(Book_Name=Book_Name)[0]
        obj=models.Electronics()
        obj.garantee=form.cleaned_data['garantee']
        obj.product_Name=form.cleaned_data['product_name']
        obj.product_price=form.cleaned_data['product_price']
        obj.product_brand=form.cleaned_data['product_brand']
        obj.product_models=form.cleaned_data['product_models']
        obj.description_text=form.cleaned_data['description_text']
        obj.user_id=request.user
        # obj.store_id = 'No store'
        obj.save()
        # obj.sold=False
        # obj.of_shop=False
        # obj.quantity=1

        # print(obj.Course_Id)
        # print(User.is_authenticated,User.is_active,User.first_name,request.user)
        return redirect('/first_app/Electronicview')


    return render(request,'first_app/bookEnter.html',{"form":form,'title':"Electronic"})

@login_required
def profile(request,pk):
    user_id = models.User.objects.filter(username=pk)[0]
    user = models.User1.objects.filter(login_id=user_id.id)[0]
    booksold=models.Shopping_Basket.objects.filter(user_id=user_id.id)
    x=[]
    for i in booksold:
        book=models.Books.objects.filter(Book_Name=i.books)[0]
        user1=models.User1.objects.filter(login_id=i.user_id)[0]
        dic={'book':book.Book_Name,'user_name':user1.Email_Id,'dop':i.date_of_purchase}
        print(user1.Email_Id)
        x.append(dic)
    return render(request, 'first_app/profile.html', {'f_name':user.f_name,'m_name':user.m_name,'l_name':user.l_name,'Hostel_Type':user.Hostel_Type,'Block':user.Block,'Email_Id':user.Email_Id,'DOB':user.DOB,'age':user.age,"x": x})



class ElectronicListView(ListView):
    model=models.Electronics

    def get_queryset(self,*args,**kargs):
        qs=super(ElectronicListView,self).get_queryset(*args,**kargs)
        qs=qs.filter(sold=False)
        print("1 Yes")
        return qs

class SportListView(ListView):
    model=models.Sports
    def get_queryset(self,*args,**kargs):
        qs=super(SportListView,self).get_queryset(*args,**kargs)
        qs=qs.filter(sold=False)
        print("1 Yes")
        return qs


class ElectronicDetail(DetailView):
    model=models.Books

class SportDetail(DetailView):
    model=models.Books


@login_required
def ElectronicBuyConfirmed(request,pk):
    temp=models.Electronics.objects.filter(product_id=pk)[0]
    temp.sold=True
    print(temp.user_id)
    user_id=models.User.objects.filter(username=temp.user_id)[0]
    user = models.User1.objects.filter(login_id=user_id.id)[0]
    # print(user)
    param={'product_name':temp.product_name,'descrition':temp.description_text,'product_price':temp.product_price,'product_brand':temp.product_brand,'product_models':temp.product_models,'garantee':temp.garantee,'user_name':user.f_name,'user_middle_name':user.m_name,'user_last_name':user.l_name,'user_Hostel_Type':user.Hostel_Type,'user_Block':user.Block,"user_Email_ID":user.Email_Id}
    temp.save()
    basket=models.Shopping_Basket()
    basket.user_id=user_id
    basket.electories_items=temp
    basket.save()
    return render(request,'first_app/electronic_buy.html',param)


@login_required
def SportsBuyConfirmed(request,pk):
    temp=models.Sports.objects.filter(product_id=pk)[0]
    temp.sold=True
    # print(temp.user_id)
    user_id=models.User.objects.filter(username=temp.user_id)[0]
    user = models.User1.objects.filter(login_id=user_id.id)[0]
    # print(user)
    param={'product_name':temp.item_name,'descrition':temp.descrition_text,'product_price':temp.item_price,'user_name':user.f_name,'user_middle_name':user.m_name,'user_last_name':user.l_name,'user_Hostel_Type':user.Hostel_Type,'user_Block':user.Block,"user_Email_ID":user.Email_Id}
    temp.save()
    basket=models.Shopping_Basket()
    basket.user_id=user_id
    basket.sports_items=temp
    basket.save()
    return render(request,'first_app/sport_buy.html',param)

def BookDetail(request,pk):
    temp=models.Books.objects.filter(Book_Id=pk)[0]
    temp.sold=True
    print(temp.user_id)
    user_id=models.User.objects.filter(username=temp.user_id)[0]
    user = models.User1.objects.filter(login_id=user_id.id)[0]
    # print(user)
    param={'book_name':temp.Book_Name,'book_descrition':temp.Descrition,'book_price':temp.Book_Price,'book_edition':temp.Edition,'book_publication':temp.Publisher,'user_name':user.f_name,'user_middle_name':user.m_name,'user_last_name':user.l_name,'user_Hostel_Type':user.Hostel_Type,'user_Block':user.Block,"user_Email_ID":user.Email_Id}
    temp.save()
    basket=models.Shopping_Basket()
    basket.user_id=user_id
    basket.books=temp
    basket.save()
    return render(request,'first_app/books_detail.html',param)