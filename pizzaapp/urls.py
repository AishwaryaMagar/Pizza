from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='homePage'),
    path('admin/', views.adminLoginView, name='adminLoginPage'),
    path('adminauthenticate/', views.authenticateAdmin),
    path('admin/homepage/',views.adminHomePageView, name="adminHomePage"),
    path('admin/logout/', views.logoutadmin),
    path('addpizza/', views.addPizza),
    path('deletepizza/<int:pizzapk>/', views.deletePizza),
    path('signupuser/', views.signUpUser),
    path('loginuser/', views.userLoginView, name="userloginpage"),
    path('customer/welcome/', views.customerview, name="customerpage"),
    path('customer/authenticate/', views.authenticateUser),
    path('userlogout/', views.userlogout),
    path('placeorder/', views.placeorder),
    path('userorder/', views.userorder),
    path('adminorder/', views.adminorders),
    path('acceptorder/<int:orderpk>/', views.acceptorder),
    path('declineorder/<int:orderpk>/', views.declineorder)
]