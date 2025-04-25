"""
URL configuration for project01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp.views import order
from myapp.views import World
from myapp.views import About
from myapp.views import Flavour_view
from myapp.views import Add_cart
from myapp.views import Location
from myapp.views import Blog
from myapp.views import Login
from myapp.views import Forgot
from myapp.views import Signup
from myapp.views import Logout
from myapp.views import PasswordResetSent
from myapp.views import PasswordReset



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',World),
    path('order/',order),
    path('About/',About),
    path('Flavour/',Flavour_view),
    path('Add_cart/',Add_cart),
    path('Location/',Location),
    path('Blog/',Blog),
    path('Login/',Login),
    path('Forgot/',Forgot),
    path('Signup/',Signup),
    path('Logout/',Logout),
    
    path('password-reset-sent/<str:reset_id>/',PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/',PasswordReset, name='reset-password'),


]
