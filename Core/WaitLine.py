from asyncio.windows_events import NULL
from datetime import datetime
from math import floor
from operator import indexOf
from re import search
from typing import List
from Core.models import Service,Ticket

class WaitLine():

    line = list()
    timeWaiting = list()
    typeOrder = list()

    def __init__(self):
        self.loadLine()

    def addAndOrderClientToLine(self,ticketId):
        self.line.append(ticketId)
        self.typeOrder.append(self.__getType(ticketId))
        self.timeWaiting.append(self.__calcWait(ticketId))

        self.__updateTimeWaiting()

        
        self.__sortByTimeWaiting()

    def addClientToLine(self,ticketId):
        
        self.line.append(ticketId)
        self.typeOrder.append(self.__getType(ticketId))
        self.timeWaiting.append(self.__calcWait(ticketId))

    def getNextTurn(self,Teller):

        nextTurn = None
        typeTeller = Service.objects.filter(service_id=Teller).values().first()
        if len(self.line) == 0:
            None
        else:

            for i in self.line:
                aux = indexOf(self.line,i)
                if self.typeOrder[aux] == typeTeller["serviceType"]:
                    nextTurn = i
                    self.__eraseTurnFromLine(aux)

            ##for i in range(0 , len(self.typeOrder) - 2 ):
              ##  x = self.typeOrder
                ##y = typeTeller["serviceType"]
                ##if self.typeOrder[i] == typeTeller["serviceType"]:
                ##    nextTurn = self.line[i]
                ##    self.__eraseTurnFromLine(i)

            if nextTurn == None:
                nextTurn = self.line[0]
                self.__eraseTurnFromLine(0)
        
        search = Ticket.objects.get(id=nextTurn)
        search.state = 1
        search.serviceId = Service.objects.get(service_id = typeTeller["service_id"])
        search.save()
        
        return Ticket.objects.filter(id=nextTurn).values().first()

    def returnLine(self):
        returnArray = list()
        searchticket = ''
        if len(self.line) > 0:
            for i in self.line:
                searchticket = Ticket.objects.filter(id=i).values().first()
                returnArray.append(searchticket)
            return returnArray
        else: 
            return None

    def loadLine(self):
        toload = Ticket.objects.filter(state = 0).values()
        for i in toload:
            if i["id"] in self.line:
                pass
            else:
                self.addClientToLine(i["id"])

        self.__updateTimeWaiting()

        
        self.__sortByTimeWaiting()

    def getarrays(self):
        arrays = list()
        arrays.append(self.line)
        arrays.append(self.typeOrder)
        arrays.append(self.timeWaiting)
        return arrays

    def __eraseTurnFromLine(self, turn):
            self.line.pop(turn)
            self.timeWaiting.pop(turn)
            self.typeOrder.pop(turn)

    def __sortByTimeWaiting(self):
        size = len(self.timeWaiting)
        maxvalue = max(self.timeWaiting) + 1
        timeOrder = [0] * size
        lineOrder = [0] * size
        typeOrder = [0] * size

        # Initialize count array
        count = [0] * maxvalue

        # Store the count of each elements in count array
        for i in range(0, size):
            y = len(count)
            x = self.timeWaiting[i]
            count[self.timeWaiting[i]] += 1

        # Store the cummulative count
        for i in range(1, maxvalue):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        i = size - 1
        while i >= 0:
            timeOrder[count[self.timeWaiting[i]] - 1] = self.timeWaiting[i]
            lineOrder[count[self.timeWaiting[i]] - 1] = self.line[i]
            typeOrder[count[self.timeWaiting[i]] - 1] = self.typeOrder[i]
            count[self.timeWaiting[i]] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            self.timeWaiting[i] = timeOrder[i]
            self.typeOrder[i] = typeOrder[i]
            self.line[i] = lineOrder[i]


    def __sortByTipeOrder(self):
        size = len(self.typeOrder)
        maxvalue = max(self.typeOrder) + 1
        timeOrder = [0] * size
        lineOrder = [0] * size
        typeOrder = [0] * size

        # Initialize count array
        count = [0] * maxvalue

        # Store the count of each elements in count array
        for i in range(0, size):
            count[self.typeOrder[i]] += 1

        # Store the cummulative count
        for i in range(1, maxvalue):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        i = size - 1
        while i >= 0:
            timeOrder[count[self.typeOrder[i]] - 1] = self.timeWaiting[i]
            lineOrder[count[self.typeOrder[i]] - 1] = self.line[i]
            typeOrder[count[self.typeOrder[i]] - 1] = self.typeOrder[i]
            count[self.typeOrder[i]] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            self.timeWaiting[i] = timeOrder[i]
            self.typeOrder[i] = typeOrder[i]
            self.line[i] = lineOrder[i]
        

    
    def __calcWait(self, ticketId):
        selectedTicket = Ticket.objects.filter(id=ticketId).values().first()
        timeInWaiting = self.__actualTime() - self.__timeToInt(selectedTicket["arrivalDate"],selectedTicket["arrivalTime"])
        if timeInWaiting < 0:
            return -timeInWaiting
        else:
            return timeInWaiting
    
    def __actualTime(self):
        time = datetime.utcnow()
        intTime = time.year * 100000 + time.month * 10000 + time.day * 1000 + time.hour * 100 + time.minute * 10 + time.second
        return intTime

    def __timeToInt(self, date, time):
        yyyy, mn, dy = date.year, date.month, date.day
        hh, mm , ss = time.hour, time.minute, time.second
        intTime = yyyy * 100000 + mn * 10000 + dy * 1000 + hh * 100 + mm * 10 + floor(ss)
        return intTime
    
    def __getType(self, lineid):
        ticketService = Ticket.objects.filter(id=lineid).values().first()
        ServiceToSearch = Service.objects.filter(service_id=ticketService["serviceId_id"]).values().first()
        return ServiceToSearch["serviceType"]

    def __updateTimeWaiting(self):

        for i in self.timeWaiting:
            for j in self.line:
                i = self.__calcWait(j)
    
    
    
