"""SDP2_PMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import Realestate.views
import Stationery.views
import Travel.views
import electronics.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',electronics.views.elec, name='home'),
    path('electric',electronics.views.electric,name='electronics'),
    path('realme',electronics.views.real,name='realme'),
    path('apple', electronics.views.apple, name='apple'),
    path('epson', electronics.views.epson, name='epson'),
    path('elect',electronics.views.ellec,name='elect'),
    path('about',electronics.views.about,name='about'),
    path('login',electronics.views.loginPage,name='login'),
    path('logout',electronics.views.logoutUser,name='logout'),
    path('register',electronics.views.register,name='register'),
    path('travel', Travel.views.trav, name='travel'),
    path('stationery', Stationery.views.stationerys, name='stationery'),
    path('payment',electronics.views.payment,name='payment'),
    path('real',Realestate.views.reals,name='real'),
    path('contact',electronics.views.contact,name='contact'),
]
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
