from datetime import datetime,timedelta
from math import floor
from operator import indexOf
from re import search
from django.db.models import Count 
from Core.models import Service,Ticket


def useByCashier(location):

    cashiers = Ticket.objects.filter(LocationId=location).values('serviceId').annotate(count= Count('serviceId')).order_by('count')

    if cashiers.exists():
        return list(cashiers)
    else: 
        return list()

def clientsByDay(location,date):

    cashiers = Ticket.objects.filter(LocationId=location,arrivalDate=date).values('serviceId').annotate(count= Count('serviceId')).order_by('serviceId')

    totalClients = 0

    if cashiers.exists():
        cashiersList = list(cashiers)
        for i in cashiersList:
            totalClients += i["count"]
        return list([totalClients,cashiersList])
    else:
        return list([0,"There are no clients on the specified Day"])

def clientsByMonth(location,month):

    searchMonth = '-'+month+'-'

    cashiers = Ticket.objects.filter(LocationId=location,arrivalDate__icontains=searchMonth).values('serviceId').annotate(count= Count('serviceId')).order_by('serviceId')

    totalClients = 0

    if cashiers.exists():
        cashiersList = list(cashiers)
        for i in cashiersList:
            totalClients += i["count"]
        return list([totalClients,cashiersList])
    else:
        return list([0,"There are no clients on the specified month"])

def avgTimeByLocation(location):
    
    timeWaiting = list()

    search = list(Ticket.objects.filter(LocationId=location).values('arrivalTime','updateTime'))

    if len(search) == 0:
        return "0"

    for i in search:
        timeWaiting.append(timedifference(i["arrivalTime"],i["updateTime"]))

    average = floor(sum(timeWaiting)/len(timeWaiting))

    averagetime = timedelta(seconds=average)

    
    return str(averagetime)



def timeToInt(time):
        hh, mm , ss = time.hour, time.minute, time.second
        intTime = hh * 3600 + mm * 60 + floor(ss)
        return intTime


def timedifference(arrival,end):
    difference=timeToInt(arrival)-timeToInt(end)
    if difference < 0:
        return -difference
    else:
        return difference
