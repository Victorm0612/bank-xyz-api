"""bankxyzapi URL Configuration

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
from django.contrib import admin
from django.urls import path
from Core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createUser/', createUsr),
    path('readUser/<str:docNumber>/', readUsr),
    path('readUser/', readAllUsr),
    path('updateUser/', modifyUsr),
    path('deleteUser/<str:idToDelete>/', delUsr),
    path('createTeller/', createTeller),
    path('readTeller/<str:name>/', readTeller),
    path('updateTeller/', modifyTeller),
    path('deleteTeller/<str:idToDelete>/', delTeller),
    path('createService/', createServ),
    path('readService/<str:serviceName>/', readServ),
    path('updateService/', modifyServ),
    path('deleteService/<str:idToDelete>/', delServ),
    path('createTicket/', createTick),
    path('readTicket/<str:orderNumber>/', readTick),
    path('updateTicket/', modifyTick),
    path('deleteTicket/<str:idToDelete>/', delTick),

]
