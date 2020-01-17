from django.db import models
from django.utils import timezone
import datetime
##from django.urls import reverse
from django.urls import path
from django.contrib.auth.models import User
#Create your models here.
HOSTEL_TYPE=(
        ('m',"Male"),
        ('f',"Female"),
    )


# class Logins(models.Model):
#     login_id = models.CharField(
#         max_length=20, primary_key=True,null=False,default='user')
#
#     login_password = models.CharField(max_length=20, null=False,default='123')
#     sec_ans1 = models.CharField(max_length=15, null=False,default='123')
#     sec_ans2 = models.CharField(max_length=15, null=False,default='123')
#
#     def __str__(self):
#         return self.login_id

class User1(models.Model):
    id=models.AutoField(primary_key=True)
    login_id = models.OneToOneField(User,
                                   on_delete=models.CASCADE)
    f_name=models.CharField(max_length=10,
                               null=False)
    m_name = models.CharField(max_length=10,
                                 null=False)
    l_name = models.CharField(max_length=10,
                                 null=False)
    Hostel_Type = models.CharField(max_length=1,
                                      default='m',
                                      choices=HOSTEL_TYPE)
    Block=models.CharField(max_length=1,default='G',null=False)
    Email_Id=models.EmailField(unique=True)
    DOB=models.DateField(null=True,default='2000-01-01')
    # phone_no=models.CharField(max_length=13)

    @property
    def age(self):
        if(self.DOB):
            now=list(map(int,(str(datetime.datetime.now()).split()[0]).split("-")))
            dob=list(map(int,str(self.DOB).split("-")))
            if(now[0]>dob[0]):
                if(now[1]>dob[1]):
                    return now[0]-dob[0]
                elif(now[1]==dob[1]):
                    if(now[2]>=dob[2]):
                        return now[0] - dob[0]
                return now[0] - dob[0] -1
        return "Invalid"
    def __str__(self):
        return self.f_name


class Courses(models.Model):
    course_code=models.CharField(max_length=12,
        primary_key=True)
    couse_name=models.CharField(max_length=25,unique=True)
    school=models.CharField(max_length=15,null=False)
    def __str__(self):
        return self.couse_name

class Stores(models.Model):
    store_id=models.AutoField(primary_key=True)
    store_name=models.CharField(max_length=20,null=False)
    city=models.CharField(max_length=15,default="Vellore",null=False)
    Building_no=models.CharField(max_length=15,null="True")
    def __str__(self):
        return self.store_name

class Books(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Book_Id=models.AutoField(primary_key=True)
    Course_Id=models.ForeignKey(Courses,
                                null=True,
                                on_delete=models.SET_NULL,
                                default = "No Course"
                                )
    Book_Name=models.CharField(max_length=35,
                               null=False)
    Book_Price=models.IntegerField(null=False,
                                   default=True)
    Publisher=models.CharField(max_length=25,
                               null=False)
    Edition=models.CharField(max_length=25,
                             null=True)

    Descrition=models.CharField(
        max_length=100,
        null=True
    )
    sold=models.BooleanField(default=False)
    # of_shop = models.BooleanField(default=False)
    # store_id=models.ForeignKey(Stores,on_delete=models.CASCADE,null=True,default=1)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return self.Book_Name

    def get_absolute_url(self):
        return reverse('first_app:test',kwargs={'id':self.Book_Id})



class StoreManager(models.Model):
    stores_id=models.OneToOneField(
        Stores,
        on_delete=models.CASCADE
    )
    managers_name=models.CharField(max_length=35,null=False)
    manager_mobile=models.IntegerField(null=False)
    manager_email=models.URLField(
        unique=True
    )
    manager_address=models.CharField(max_length=25)
    def __str__(self):
        return self.manager_name




class Electronics(models.Model):
    user_id = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=35,null=False)
    product_price=models.IntegerField(default=250,null=False)
    product_brand=models.CharField(max_length=25,null=False)
    product_models=models.CharField(max_length=25,null=False)
    description_text=models.CharField(max_length=100,
                                      default="These is for sell")
    garantee=models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    # of_shop = models.BooleanField(default=False)
    # store_id = models.ForeignKey(Stores, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name

class Sports(models.Model):
    user_id = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    item_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=35,null=False)
    item_price=models.IntegerField(null=False)
    descrition_text=models.CharField(max_length=100,
                                     default="These is for sell")
    sold = models.BooleanField(default=False)
    # of_shop = models.BooleanField(default=False)
    # store_id = models.ForeignKey(Stores, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item_name



class Shopping_Basket(models.Model):
    basket_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    sports_items=models.ForeignKey(Sports,on_delete=models.CASCADE,null=True)
    electories_items=models.ForeignKey(Electronics,on_delete=models.CASCADE,null=True)
    books=models.ForeignKey(Books,on_delete=models.CASCADE,null=True)
    date_of_purchase=models.DateField(default=timezone.now)
    time_of_purchase=models.TimeField(auto_now=True,auto_now_add=False)


# class Sells(models.Model):
#     store=models.ForeignKey(Stores,on_delete=models.CASCADE)
#     books=models.ManyToManyField(Books)
#     sports_items = models.ManyToManyField(Sports)
#     electories_items = models.ManyToManyField(Electronics)
#     def __str__(self):
#         return f"Item of-{self.store}"


