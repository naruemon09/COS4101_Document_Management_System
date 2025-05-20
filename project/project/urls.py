"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from document import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginPage,name="login"),
    path('signout',views.signout,name="signout"),
    path('signUp',views.signUp,name="signUp"),
    path('register', views.register, name="register"),
    path('forgetPassword',views.forgetPassword,name="forgetPassword"),
    path('fillEmail', views.fillEmail, name="fillEmail"),
    path('otpPassword',views.otpPassword,name="otpPassword"),
    path('rePassword',views.rePassword,name="rePassword"),
    path('menu',views.menu,name="menu"),
    path('menu/receive',views.receive,name="receive"),
    path('menu/send',views.send,name="send"),
    path('menu/search',views.search,name="search"),
    path('menu/search/viewDoc',views.viewDoc,name="viewDoc"),
]
