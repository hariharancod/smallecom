"""
URL configuration for smallecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

#from smallecom.ecom_app import views
from ecom_app.views import *
from django.conf import settings
from django.conf.urls.static import static 
#from smallecom.smallecom import settingsno
from django.contrib.auth import views as auth_views

from ecom_app.views import *
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',Index.as_view()),
    path('ecom/',Index_react.as_view(),name='index'),
    path('account/',Accounts.as_view(),name='Accounts'),
    path('product/',Products.as_view(),name='Product'),
    path('addcart/',Addcarts.as_view(),name='Addcarts'),
    path('login/',Login_auth.as_view(),name='Login_auth'),
    path('delete/',Deletes.as_view()),
     path('updates/',Updates.as_view()),
     path('my_cart/',My_cart.as_view()),
     path('add_deletes/',Add_deletes.as_view()),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)