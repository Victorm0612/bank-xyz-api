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
from django.conf import settings
from django.conf.urls.static import static
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
    path('createLocation/', createLocation),
    path('readLocation/<str:name>/', readLocation),
    path('readLocation/', readAllLocation),
    path('updateLocation/', modifyLocation),
    path('deleteLocation/<str:idToLocation>/', delLocation),
    path('createService/', createServ),
    path('readService/', readAllServ),
    path('readService/<str:serviceName>/', readServ),
    path('updateService/', modifyServ),
    path('deleteService/<str:idToDelete>/', delServ),
    path('createTicket/', createTick),
    path('readTicket/<str:orderNumber>/', readTick),
    path('updateTicket/', modifyTick),
    path('deleteTicket/<str:idToDelete>/', delTick),
    path('login/', loginUser),
    path('refresh/',refreshUser),
    path('createUserAdmin/',createUserAdmin),
    path('getLine/<str:locationId>/', getLine),
    path('getNextTurn/<str:servicetype>/<str:locationId>/',getNextTurn),
    path('getLineArrays/<str:locationId>/',getLineArrays),
    path('getLocationUseData/<str:locationId>/',getLocationUseData),
    path('getAvgTimeByLocation/<str:locationId>/',getAvgTimeByLocation),

    path('getClientsByDay/<str:locationId>/<str:date>/',getClientsByDay),
    path('getClientsByMonth/<str:locationId>/<str:month>/',getClientsByMonth)


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
