from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name='first_app'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^registeruser/',views.usercreate,name='userform'),
    url(r'^bookEnter/',views.bookEnter,name='bookEnter'),
    url(r'^electronicEnter/',views.electronicEnter,name='electronicEnter'),
    url(r'^sportEnter/',views.sportEnter,name='sportEnter'),
    url(r'^storeEnter/', views.StoreEnter, name='storeEnter'),
    url(r'^profile/(?P<pk>[a-zA-z-._0-9]+)/',views.profile,name="Profile"),
    url('^basic/',views.basic,name="basic"),
    url(r'^bookview/$',views.BookListView.as_view(),name="BookView"),
    url(r'^electronicview/$',views.ElectronicListView.as_view(),name="ElectronicView"),
    url(r'^sportview/$',views.SportListView.as_view(),name="SportView"),
    url(r'^bookview/(?P<pk>\d+)/$',views.BookDetail,name='BookDetail'),
    url(r'^Electronicview/(?P<pk>\d+)/$',views.ElectronicDetail.as_view(),name='ElectronicDetail'),
    url(r'^Sportview/(?P<pk>\d+)/$',views.SportDetail.as_view(),name='SportDetail'),
    url(r'^bookbuy/(?P<pk>\d+)/$',views.BookBuy.as_view(),name='BookBuy'),
    url(r'^book_buy_confirmed/(?P<pk>\d+)/$',views.bookBuyConfirmed,name='BookBuyConfirmed'),
    url(r'^Electronic_buy_confirmed/(?P<pk>\d+)/$',views.ElectronicBuyConfirmed,name='ElectronicBuyConfirmed'),
    url(r'^sportbuy/(?P<pk>\d+)/$',views.SportsBuyConfirmed,name='SportsBuyConfirmed'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='first_app/login.html'),name="login"),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name='first_app/logout.html'),name="logout"),
]
