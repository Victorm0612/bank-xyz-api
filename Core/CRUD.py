from ast import If, arg
from datetime import datetime
from re import search
from Core.models import *
from django.contrib.auth.hashers import make_password

#
# creates a new user in the table User
#   args is an array of the arguments received
#

def CreateUser(args):
    # args order firstName, lastName, docType, docNumber, role, email, password
    if User.objects.filter(docNumber = args[3]).exists():
        return False
    else:
        newUser = User(firstName = args[0],lastName = args[1],docType = args[2], docNumber = args[3], role = int(args[4]),email = args[5], password = make_password(args[6],salt=None,hasher='default'))
        newUser.save() 
        return True

#
# search for a user or users in the table User
#   args is an array of the arguments received
#

def ReadUser(args):
    search = User.objects.filter(docNumber__icontains = args[0])
    search.order_by('id')
    return search.values()


def ReadAllUser():
    search = User.objects.all()
    search.order_by('id')
    return search.values()
#
#  Update a User in the table User
#   args is an array of the arguments received
#
def UpdateUser(args):

     # args order id, firstName, lastName, docType, docNumber, role, email, password
    if  User.objects.filter(id = args[0]).exists():
        userToMod= User.objects.get(id = args[0])
        if args[1] != '':
            userToMod.firstName = args[1]
        
        if args[2] != '':
            userToMod.lastName = args[2]
        
        if args[3] != '':
            userToMod.docType = args[3]
        
        if args[4] != '':
            userToMod.docNumber = args[4]
        
        if args[5] != '':
            userToMod.role = args[5]
        
        if args[6] != '':
            userToMod.email = args[6]
        
        if args[7] != '':
            userToMod.password = make_password(args[7],salt=None,hasher='default')

        userToMod.save()
        return True
    else : 
        return False
    




    
    
#
# Delete a User in the table User
#   args is an array of the arguments received
#
def DeleteUser(args):
    
    if User.objects.filter(id = args[0]).exists() :
        userToDelete = User.objects.get(id=args[0])
        userToDelete.delete()
        return True
    else : 
        return False
        
#
# creates a new location in the table BankTeller
#   args is an array of the arguments received
#
def CreateLocation(args):
    # args order name
    if Location.objects.filter(name = args[0]).exists():
        return False
    else: 
        newLocation = Location(name=args[0])
        newLocation.save()
        return True

#
# search for one or more locations in the table BankTeller
#   args is an array of the arguments received to do the search
#
def ReadLocation(args):
    # args order name
    search = Location.objects.filter(name__icontains = args[0])
    search.order_by('id')
    return search.values()

def ReadAllLocation():
    # args order name
    search = Location.objects.all()
    search.order_by('id')
    return search.values()
    
#
#  Update a location in the table BankTeller
#   args is an array of the arguments received
#
def UpdateLocation(args):
    # args order id, name
    if Location.objects.filter(id = args[0]).exists():
        locationToMod= Location.objects.get(id = args[0])
        if args[1] != '':
            locationToMod.name = args[1]
        locationToMod.save()
        return True
    else:
        return False

    
    
#
# Delete a location in the table BankTeller
#   args is an array of the arguments received
#
def DeleteLocation(args):
    # args order id
    if Location.objects.filter(id = args[0]).exists() :
        locationToDelete = Location.objects.get(id=args[0])
        locationToDelete.delete()
        return True
    else : 
        return False
        
    

#
# creates a new bank teller in the table BankTeller
#   args is an array of the arguments received
#
def CreateBankTeller(args):
    # args order name
    if BankTeller.objects.filter(name = args[0]).exists():
        return False
    else: 
        newTeller = BankTeller(name=args[0])
        newTeller.save()
        return True

#
# search for one or more bank tellers in the table BankTeller
#   args is an array of the arguments received to do the search
#
def ReadBankTeller(args):
    # args order name
    search = BankTeller.objects.filter(name__icontains = args[0])
    search.order_by('id')
    return search.values()
    
#
#  Update a bank teller in the table BankTeller
#   args is an array of the arguments received
#
def UpdateBankTeller(args):
    # args order id, name
    if BankTeller.objects.filter(id = args[0]).exists():
        tellerToMod= BankTeller.objects.get(id = args[0])
        if args[1] != '':
            tellerToMod.name = args[1]
        tellerToMod.save()
        return True
    else:
        return False

    
    
#
# Delete a bank teller in the table BankTeller
#   args is an array of the arguments received
#
def DeleteBankTeller(args):
    # args order id
    if BankTeller.objects.filter(id = args[0]).exists() :
        tellerToDelete = BankTeller.objects.get(id=args[0])
        tellerToDelete.delete()
        return True
    else : 
        return False
        
    
#
# creates a new Servive in the table Service
#   args is an array of the arguments received
#
def CreateService(args):
    # args order serviceName, description, serviceType, teller_id_id
    if Service.objects.filter(serviceName = args[0],description = args[1]).exists():
        return False
    else: 
        newService = Service(serviceName=args[0],description=args[1],serviceType=int(args[2]),teller_id_id=int(args[3]))
        newService.save()
        return True

#
# search for one or more Services in the table Service
#   args is an array of the arguments received to do the search
#
def ReadAllService():

    # args order serviceType, teller_id_id
    search = Service.objects.all()
    search.order_by('service_id')
    return search.values()

def ReadService(args):

    # args order serviceType, teller_id_id
    search = Service.objects.filter(serviceName__icontains = args[0])
    search.order_by('service_id')
    return search.values()
    
#
#  Update a Service in the table Service
#   args is an array of the arguments received
#
def UpdateService(args):

    if Service.objects.filter(service_id = args[0]).exists():
        ServiceToMod= Service.objects.get(service_id = args[0])

        if args[1] != '':
            ServiceToMod.serviceName = args[1]
        
        if args[2] != '':
            ServiceToMod.description = args[2]
        
        if args[3] != '':
            ServiceToMod.serviceType = args[3]
        
        if args[4] != '':
            ServiceToMod.teller_id_id = BankTeller.objects.get(id = int(args[4]))
        ServiceToMod.save()
        return True
    else:
        return False

    
#
# Delete a Service in the table Service
#   args is an array of the arguments received
#
def DeleteService(args):

    if Service.objects.filter(id = args[0]).exists() :
        serviceToDelete = Service.objects.get(id=args[0])
        serviceToDelete.delete()
        return True
    else : 
        return False
    

#
# creates a new ticket in the table Ticket
#   args is an array of the arguments received
#
def CreateTicket(args):
    time = datetime.now()
    # args order : orderNumber, state, serviceId_id, userId_id
    if Ticket.objects.filter(orderNumber=args[0]).exists():
        return [False,args[0]]
    else: 
        service = Service.objects.get(service_id=args[2])
        user = User.objects.get(id=args[3])
        location = Location.objects.get(id=args[4])
        newTicket = Ticket(
                        orderNumber=args[0],
                        state=int(args[1]),
                        serviceId=service,
                        userId=user,
                        LocationId=location
                        )
        newTicket.save()
        search = Ticket.objects.filter(orderNumber=args[0]).values().first()
        return [True,search]


#
# search for one or more Tickets in the table Ticket
#   args is an array of the arguments received to do the search
#
def ReadTicket(args):

    search = Ticket.objects.filter(orderNumber__icontains = int(args[0]))
    search.order_by('id')
    return search.values()


#
# search and returns the Id of one Ticket
#   ordernumber is the number of order we want to search
#
def getTicketId(numbertosearch):
    search = Ticket.objects.filter(orderNumber = int(numbertosearch)).values().first()
    return search["id"]
#
#  Update a Ticket in the table Ticket
#   args is an array of the arguments received
#
def UpdateTicket(args):
    print(Ticket.objects.filter(id = args[0]).exists())
    if Ticket.objects.filter(id = args[0]).exists():

        ticketToMod= Ticket.objects.get(id = args[0])

        if args[1] != '':
            ticketToMod.orderNumber = args[1]
        
        if args[2] != '':
            ticketToMod.state = int(args[2])
        
        if args[3] != '':
            ticketToMod.arrivalDate = args[3]
        
        if args[4] != '':
            ticketToMod.arrivalTime = args[4]
        
        if args[5] != '':
            ticketToMod.serviceId = Service.objects.get(service_id = int(args[5]))
        
        if args[6] != '':
            ticketToMod.userId = User.objects.get(id = int(args[6]))

        if args[7] != '':
            ticketToMod.LocationId = Location.objects.get(id = int(args[7]))

        ticketToMod.save()
        return True
    else:
        return False
    
#
# Delete a Ticket in the table Ticket
#   args is an array of the arguments received
#
def DeleteTicket(args):
    if Ticket.objects.filter(id = args[0]).exists() :
        ticketToDelete = Ticket.objects.get(id=args[0])
        ticketToDelete.delete()
        return True
    else : 
        return False




def getNumberId(numberId):
    userSearch=User.objects.filter(docNumber=numberId).values().first()
    return userSearch["id"]

def getTellerByServiceType(type):
    serviceSearch=Service.objects.filter(serviceType=type).values().first()
    return serviceSearch["service_id"]

def getOrderNumberByServicetype(type):
    search = None
    if type == 0:

        if Ticket.objects.filter(orderNumber__icontains="G").exists():
            search = Ticket.objects.filter(orderNumber__icontains="G").values()
            search.order_by('id')
            split = search.last()["orderNumber"].split("G")
            number = int(split[1]) + 1
            return "G" + str(number)
        else: return "G1"

    elif type == 1:
        if Ticket.objects.filter(orderNumber__icontains="I").exists():
            search = Ticket.objects.filter(orderNumber__icontains="I").values()
            search.order_by('id')
            split = search.last()["orderNumber"].split("I")
            number = int(split[1]) + 1
            return "I" + str(number)
        else: return "I1"
    elif type == 2:
        if Ticket.objects.filter(orderNumber__icontains="S").exists():
            search = Ticket.objects.filter(orderNumber__icontains="S").values()
            search.order_by('id')
            split = search.last()["orderNumber"].split("S")
            number = int(split[1]) + 1
            return "S" + str(number)
        else: return "S1"
            
    elif type == 3:
        if Ticket.objects.filter(orderNumber__icontains="D").exists():
            search = Ticket.objects.filter(orderNumber__icontains="D").values()
            search.order_by('id')
            split = search.last()["orderNumber"].split("D")
            number = int(split[1]) + 1
            return "D" + str(number)
        else: return "D1"
    else:
        if Ticket.objects.filter(orderNumber__icontains="V").exists():
            search = Ticket.objects.filter(orderNumber__icontains="V").values()
            search.order_by('id')
            split = search.last()["orderNumber"].split("V")
            number = int(split[1]) + 1
            return "V" + str(number)
        else: return "V1"