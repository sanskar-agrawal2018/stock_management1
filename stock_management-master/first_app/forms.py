from django import forms
from first_app.models import User1,Books,Stores,Electronics,Sports
from django.contrib.auth.models import User
class RegisterUserForm(forms.ModelForm):
    class Meta():
        model=User1
        fields=('f_name','m_name','l_name','Hostel_Type','Block','Email_Id','DOB')

class Loginform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','password')

class BookEnterForm(forms.ModelForm):
    class Meta():
        model=Books
        fields='Book_Id,Course_Id,Book_Name,Book_Price,Publisher,Edition,Descrition'.split(',')


class ElectronicEnterForm(forms.ModelForm):
    class Meta():
        model=Electronics
        fields='product_id,product_name,product_price,product_brand,product_models,description_text,garantee'.split(',')

class SportEnterForm(forms.ModelForm):
    class Meta():
        model=Sports
        fields='item_name,item_price,descrition_text'.split(',')

class Storeform(forms.ModelForm):
    class Meta():
        model=Stores
        fields='__all__'

