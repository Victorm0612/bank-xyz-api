from ast import arg
from datetime import datetime
from Core.models import *

#
# creates a new user in the table User
#   args is an array of the arguments received
#

def CreateUser(args):
    # args order firstName, lastName, docType, docNumber, role, email, password
    if User.objects.filter(docNumber = args[3]).exists():
        return False
    else:
        newUser = User(firstName = args[0],lastName = args[1],docType = args[2], docNumber = args[3], role = int(args[4]),email = args[5], password = args[6])
        newUser.save() 
        return True

#
# search for a user or users in the table User
#   args is an array of the arguments received
#

def ReadUser(args):
    search = User.objects.filter(docNumber__icontains=args[0])
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
            userToMod.password = args[7]

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
        return False

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
        tellerToDelete = User.objects.get(id=args[0])
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
def ReadService(args):

    # args order serviceType, teller_id_id
    search = Service.objects.filter(serviceName__icontains = int(args[0]))
    search.order_by('id')
    return search.values()
    
#
#  Update a Service in the table Service
#   args is an array of the arguments received
#
def UpdateService(args):

    if Service.objects.filter(id = args[0]).exists():
        ServiceToMod= Service.objects.get(id = args[0])

        if args[1] != '':
            ServiceToMod.serviceName = args[1]
        
        if args[2] != '':
            ServiceToMod.description = args[2]
        
        if args[3] != '':
            ServiceToMod.serviceType = args[3]
        
        if args[4] != '':
            ServiceToMod.teller_id_id = args[4]
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
        serviceToDelete = User.objects.get(id=args[0])
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
    # args order : orderNumber, state, arrivalDate, arrivalTime, serviceId_id, userId_id
    if Ticket.objects.filter(name = args[0]).exists():
        return False
    else: 
        newTicket = Ticket(orderNumber=int(args[0]),state=int(args[1]),arrivalDate=time.date(),arrivalTime=time.time(),serviceId_id=int(args[2]),userId_id=int(args[3]))
        newTicket.save()
        return True


#
# search for one or more Tickets in the table Ticket
#   args is an array of the arguments received to do the search
#
def ReadTicket(args):

    search = Ticket.objects.filter(orderNumber__icontains = int(args[0]))
    search.order_by('id')
    return search.values()
#
#  Update a Ticket in the table Ticket
#   args is an array of the arguments received
#
def UpdateTicket(args):

    if Ticket.objects.filter(id = args[0]).exists():

        ticketToMod= Ticket.objects.get(id = args[0])

        if args[1] != '':
            ticketToMod.orderNumber = int(args[1])
        
        if args[2] != '':
            ticketToMod.state = int(args[2])
        
        if args[3] != '':
            ticketToMod.arrivalDate = args[3]
        
        if args[4] != '':
            ticketToMod.arrivalTime = args[4]
        
        if args[4] != '':
            ticketToMod.serviceId_id = int(args[5])
        
        if args[4] != '':
            ticketToMod.userId_id = int(args[6])

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
        ticketToDelete = User.objects.get(id=args[0])
        ticketToDelete.delete()
        return True
    else : 
        return False