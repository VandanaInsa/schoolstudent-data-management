"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#superuser is Admin and password is admin
from django.contrib import admin
from django.urls import path,include
from data import views

urlpatterns = [
    path( 'admin/', admin.site.urls ),
    path('',views.studentList.as_view()),
   #path( 'student/', views.studentCreate.as_view() ),
    #path( 'retrive/<int:pk>/', views.studentRetrieve.as_view() ),
    #path( 'update/<int:pk>/', views.studentUpdate.as_view() ),
    #path( 'delete/<int:pk>/', views.studentDestroy.as_view()),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))

]
