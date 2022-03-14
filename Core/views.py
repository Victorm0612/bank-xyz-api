from genericpath import exists
from Core.CRUD import *
from Core.models import *
from Core.login import login
from Core.authentication import authUsr, authTeller, authServ, authTick, authRefresh
from Core.WaitLine import WaitLine
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from bankxyzapi.settings.base import SECRET_KEY
import json
import jwt

line = None

# Create your views here.
@csrf_exempt
def createUsr(request):
    authentication = authUsr(request)
    if authentication == "Successfull" :

        req = json.load(request)
        firstName = req["firstName"]
        lastName = req["lastName"]
        doctype = req["docType"]
        docNumber = req["docNumber"]
        role = req["role"]
        email = req["email"]
        password = req["password"]
        
        send = [firstName,lastName,doctype,docNumber,role,email,password]

        if len(docNumber) < 8 or len(docNumber) > 10:
            return JsonResponse("Document Number Not Valid", safe= False, status = 404)

        if CreateUser(send):
            return JsonResponse("User Created", safe=False)
        else:
            return JsonResponse("User Couldn't Be Created", safe= False, status = 404)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)


def readUsr(request,docNumber):

    authentication = authUsr(request)
    if authentication == "Successfull" :
        
        send = [docNumber]
        searchResult = ReadUser(send)
        ret = list(searchResult)
        return JsonResponse(ret, safe=False)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)


def readAllUsr(request):

    authentication = authUsr(request)
    if authentication == "Successfull" :
        
        searchResult = ReadAllUser()
        ret = list(searchResult)

        return JsonResponse(ret, safe=False)        
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

@csrf_exempt
def modifyUsr(request):

    authentication = authUsr(request)
    if authentication == "Successfull" :

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
            return JsonResponse("User Updated",safe=False)
        else:
            return JsonResponse("User Couldn't Be Updated",safe=False, status = 404)        
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

    


@csrf_exempt
def delUsr(request,idToDelete):


    authentication = authUsr(request)
    if authentication == "Successfull" :
        
        send=[idToDelete]

        if DeleteUser(send):
            return JsonResponse("User Deleted",safe=False)
        else:
            return JsonResponse("User Couldn't Be Deleted",safe=False, status = 404)  
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

    


@csrf_exempt
def createTeller(request):
   

    authentication = authTeller(request)
    if authentication == "Successfull" :
        
        req = json.load(request)


        name = req["name"]
        
        send = [name]

        if CreateBankTeller(send):
            return JsonResponse("Teller Created", safe=False)
        else:
            return JsonResponse("Teller Couldn't Be Created", safe= False, status = 404)  
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

     

def readTeller(request, name):

    authentication = authTeller(request)
    if authentication == "Successfull" :
        
        send = [name]
        searchResult = ReadBankTeller(send)

        ret = list(searchResult)

        return JsonResponse(ret, safe=False)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

    


@csrf_exempt
def modifyTeller(request):

    authentication = authTeller(request)
    if authentication == "Successfull" :

        req = json.load(request)

    
        idTeller = req["id"]
        name = req["name"]
        
        send = [idTeller,name]

        if UpdateBankTeller(send):
            return JsonResponse("Teller Updated", safe=False)
        else:
            return JsonResponse("Teller Couldn't Be Updated", safe=False, status = 404)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)




@csrf_exempt
def delTeller(request,idToDelete):


    authentication = authTeller(request)
    if authentication == "Successfull" :
        
        send=[idToDelete]

        if DeleteBankTeller(send):
            return JsonResponse("Teller Deleted", safe=False)
        else:
            return JsonResponse("Teller Couldn't Be Deleted", safe=False, status = 404)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)


    


@csrf_exempt
def createServ(request):

    
    authentication = authServ(request)
    if authentication == "Successfull" :
        
        #### serviceName, description, serviceType, teller_id_id
        req = json.load(request)


        serviceName = req["serviceName"]
        description = req["description"]
        serviceType = req["serviceType"]
        teller_id = req["teller_id_id"]
        
        send = [serviceName,description,serviceType,teller_id]


        if CreateService(send):
            return JsonResponse("Service Created", safe=False)
        else:
            return JsonResponse("Service Couldn't Be Created", safe=False, status = 404)          
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

    

def readAllServ(request):


    authentication = authServ(request)
    if authentication == "Successfull" :
        searchResult = ReadAllService()
        ret = list(searchResult)

        return JsonResponse(ret,safe=False)        
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False)
    else : 
        return JsonResponse("Token Not Valid", safe=False)


def readServ(request,serviceName):


    authentication = authServ(request)
    if authentication == "Successfull" :

        ### serviceType, teller_id_id

        send = [serviceName]
        searchResult = ReadService(send)
        ret = list(searchResult)

        return JsonResponse(ret,safe=False)        
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

    


@csrf_exempt
def modifyServ(request):


    authentication = authServ(request)
    if authentication == "Successfull" :
        req = json.load(request)


        idService = req["service_id"]
        serviceName = req["serviceName"]
        description = req["description"]
        serviceType = req["serviceType"]
        teller_id = req["teller_id_id"]
        
        send = [idService,serviceName,description,serviceType,teller_id]
        if UpdateService(send):
            return JsonResponse("Service Updated", safe=False)
        else:
            return JsonResponse("Service Couldn't Be Updated", safe=False, status = 404)        
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)



@csrf_exempt
def delServ(request, idToDelete):

    authentication = authServ(request)
    if authentication == "Successfull" :
        

        send=[idToDelete]

        if DeleteService(send):
            return JsonResponse("Service Deleted", safe=False)
        else:
            return JsonResponse("Service Couldn't Be Deleted", safe=False, status = 404) 
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

    

@csrf_exempt
def createTick(request):

    authentication = authTick(request)
    if authentication == "Successfull" :
        global line
        #### orderNumber, state, serviceId_id, userId_id
        req = json.load(request)


        orderNumber = req["orderNumber"]
        state = req["state"]
        serviceId = req["serviceId_id"]
        userId = req["userId_id"]
        
        send = [orderNumber, state, serviceId ,userId]


        if CreateTicket(send):
            if line is None:
                line = WaitLine(getTicketId(orderNumber))
                line.loadLine()
            else:
                line.addClientToLine(getTicketId(orderNumber))
            return JsonResponse("Ticket Created", safe=False)
        else:
            return JsonResponse("Ticket Couldn't Be Created", safe=False, status = 404)        
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)




def readTick(request,orderNumber):

    authentication = authTick(request)
    if authentication == "Successfull" :

        ### orderNumber, arrivalDate, serviceId, userId_id

        send = [orderNumber]
        searchResult = ReadTicket(send)
        ret = list(searchResult)

        return JsonResponse(ret, safe=False)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)


    

@csrf_exempt
def modifyTick(request):

    authentication = authTick(request)
    if authentication == "Successfull" :
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
            line.addClientToLine(idTick)
            return JsonResponse("Ticket Updated", safe=False)
        else:
            return JsonResponse("Ticket Couldn't Be Updated", safe=False, status = 404)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)


    


@csrf_exempt
def delTick(request,idToDelete):

    authentication = authTick(request)
    if authentication == "Successfull" :

        send=[idToDelete]

        if DeleteTicket(send):
            return JsonResponse("Ticket Deleted", safe=False)
        else:
            return JsonResponse("Ticket Couldn't Be Deleted", safe=False, status = 404)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

@csrf_exempt
def getLine(request):
    global line
    authentication = authTick(request)
    if authentication == "Successfull" :
        if line is None:
            return JsonResponse("There is No Line At The Moment", safe=False, status = 404)
        else:
            actualLine = line.returnLine()

            if actualLine is None:
                return JsonResponse("There is No Line At The Moment", safe=False, status = 404)
            else:
                return JsonResponse(actualLine, safe=False)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

@csrf_exempt
def getNextTurn(request):
    global line
    authentication = authTick(request)
    if authentication == "Successfull" :
        if line is None:
            return JsonResponse("There is No Line At The Moment", safe=False, status = 404)
        else:
            actualLine = line.getNextTurn()

            if actualLine is None:
                return JsonResponse("There is No Line At The Moment", safe=False, status = 404)
            else:
                return JsonResponse(actualLine, safe=False)
    elif authentication == "Token expired":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "No Authorization Token Given":
        return JsonResponse(authentication, safe=False, status = 404)
    elif authentication == "User Not Authorized":
        return JsonResponse(authentication, safe=False, status = 404)
    else : 
        return JsonResponse("Token Not Valid", safe=False, status = 404)

    

@csrf_exempt
def loginUser(request):

    req = json.load(request)
    user = req["email"]
    password= req["password"]
    tokens = login(user,password)
    if isinstance(tokens,list):
        return JsonResponse({"access":tokens[0],"refresh":tokens[1], "docNumber": tokens[2]})
    else:
        return JsonResponse(tokens,safe=False, status = 404)

@csrf_exempt
def refreshUser(request):

    newtokens = authRefresh(request)
    if isinstance(newtokens,list):
        return JsonResponse({"access":newtokens[0],"refresh":newtokens[1]})
    else:
        return JsonResponse(newtokens,safe=False, status = 404)


@csrf_exempt
def createUserAdmin(request):
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
            return JsonResponse("User Created", safe=False)
        else:
            return JsonResponse("User Couldn't Be Created", safe= False, status = 404)


    

    


