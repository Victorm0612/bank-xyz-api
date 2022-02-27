import re
from django.shortcuts import render
from Core.CRUD import *
from Core.models import *
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json



# Create your views here.
@csrf_exempt
def createUsr(request):
    req = json.load(request)
    firstName = req["firstName"]
    lastName = req["lastName"]
    doctype = req["docType"]
    docNumber = req["docNumber"]
    role = req["role"]
    email = req["email"]
    password = req["password"]
    
    send = [firstName,lastName,doctype,docNumber,role,email,password]

    if CreateUser(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe= False)


def readUsr(request,docNumber):

    send = [docNumber]
    searchResult = ReadUser(send)
    ret = list(searchResult)

    return JsonResponse(ret, safe=False)

def readAllUsr(request):
  searchResult = ReadAllUser()
  ret = list(searchResult)

  return JsonResponse(ret, safe=False)

@csrf_exempt
def modifyUsr(request):

    req = json.load(request)

    idUser = req["id"]
    firstName = req["firstName"]
    lastName = req["lastName"]
    doctype = req["docType"]
    docNumber = req["docNumber"]
    role = req["role"]
    email = req["email"]
    password = req["password"]
    
    send = [idUser,firstName,lastName,doctype,docNumber,role,email,password]

    if UpdateUser(send):
        return JsonResponse(True,safe=False)
    else:
        return JsonResponse(False,safe=False)


@csrf_exempt
def delUsr(request,idToDelete):

    send=[idToDelete]

    if DeleteUser(send):
        return JsonResponse(True,safe=False)
    else:
        return JsonResponse(False,safe=False)


@csrf_exempt
def createTeller(request):

    req = json.load(request)


    name = req["name"]
    
    send = [name]

    if CreateBankTeller(send):
        return JsonResponse(True,safe=False)
    else:
        return JsonResponse(False,safe=False)

def readTeller(request, name):

    send = [name]
    searchResult = ReadBankTeller(send)

    ret = list(searchResult)

    return JsonResponse(ret, safe=False)


@csrf_exempt
def modifyTeller(request):

    req = json.load(request)

    
    idTeller = req["id"]
    name = req["name"]
    
    send = [idTeller,name]

    if UpdateBankTeller(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)


@csrf_exempt
def delTeller(request,idToDelete):


    send=[idToDelete]

    if DeleteBankTeller(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)


@csrf_exempt
def createServ(request):

    #### serviceName, description, serviceType, teller_id_id
    req = json.load(request)


    serviceName = req["serviceName"]
    description = req["description"]
    serviceType = req["serviceType"]
    teller_id = req["teller_id_id"]
    
    send = [serviceName,description,serviceType,teller_id]


    if CreateService(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)

def readServ(request,serviceName):

    ### serviceType, teller_id_id

    send = [serviceName]
    searchResult = ReadService(send)
    ret = list(searchResult)

    return JsonResponse(ret,safe=False)


@csrf_exempt
def modifyServ(request):

    req = json.load(request)


    idService = req["id"]
    serviceName = req["serviceName"]
    description = req["description"]
    serviceType = req["serviceType"]
    teller_id = req["teller_id_id"]
    
    send = [idService,serviceName,description,serviceType,teller_id]

    if UpdateService(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)


@csrf_exempt
def delServ(request):

    idService = request.DELETE["id"]

    send=[idService]

    if DeleteService(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)

@csrf_exempt
def createTick(request):

    #### orderNumber, state, serviceId_id, userId_id
    req = json.load(request)


    orderNumber = req["orderNumber"]
    state = req["state"]
    serviceId = req["serviceId_id"]
    userId = req["userId_id"]
    
    send = [orderNumber, state, serviceId ,userId]


    if CreateTicket(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)

def readTick(request,orderNumber):

    ### orderNumber, arrivalDate, serviceId, userId_id

    send = [orderNumber]
    searchResult = ReadTicket(send)
    ret = list(searchResult)

    return JsonResponse(ret, safe=False)


@csrf_exempt
def modifyTick(request):

    req = json.load(request)


    idTick = req["id"]
    orderNumber = req["orderNumber"]
    state = req["state"]
    arrivalDate = req["arrivalDate"]
    arrivalTime = req["arrivalTime"]
    serviceId = req["serviceId_id"]
    userId = req["userId_id"]
    
    send = [idTick, orderNumber, state, arrivalDate, arrivalTime, serviceId, userId]

    if UpdateTicket(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)


@csrf_exempt
def delTick(request):

    idTick = request.DELETE["id"]

    send=[idTick]

    if DeleteTicket(send):
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
