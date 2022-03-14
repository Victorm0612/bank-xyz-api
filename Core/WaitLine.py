from asyncio.windows_events import NULL
from datetime import datetime
from math import floor
from re import search
from typing import List
from Core.models import Service,Ticket

class WaitLine():

    line = list()
    timeWaiting = list()
    typeOrder = list()

    def __init__(self, ticketId):
        self.line.append(ticketId)
        self.timeWaiting.append(self.__calcWait(ticketId))
        self.typeOrder.append(self.__getType(ticketId))

    def addClientToLine(self,ticketId):
        self.__updateTimeWaiting()
        self.line.append(ticketId)
        self.typeOrder.append(self.__getType(ticketId))
        self.timeWaiting.append(self.__calcWait(ticketId))

        self.__sortByTimeWaiting()
        self.__sortByTipeOrder()

    def getNextTurn(self,typeTeller):

        nextTurn = None
        if len(self.line) == 0:
            None
        else:
            for i in range(len(self.typeOrder)):
                if self.typeOrder[i] == typeTeller:
                    nextTurn = self.line[i]
                    self.__eraseTurnFromLine(nextTurn)

            if nextTurn == None:
                nextTurn = self.line[0]
                self.__eraseTurnFromLine(nextTurn)
        
        return Ticket.objects.filter(id=nextTurn).values().first()

    def returnLine(self):
        returnArray = list()
        searchticket = ''
        if len(self.line) > 0:
            for i in self.line:
                searchticket = Ticket.objects.filter(id=i).values().first()
                returnArray.append(i)
            return returnArray
        else: 
            return None

    def loadLine(self):
        toload = Ticket.objects.filter(state = 0).values()
        for i in toload:
            self.addClientToLine(i["id"])

    def __eraseTurnFromLine(self, turn):
        for i in range(len(self.line)):
            if self.line[i] == turn:
                self.line.pop(i)
                self.timeWaiting.pop(i)
                self.typeOrder.pop(i)

    def __sortByTimeWaiting(self):
        size = len(self.timeWaiting)
        maxvalue = max(self.timeWaiting)
        timeOrder = [0] * size
        lineOrder = [0] * size
        typeOrder = [0] * size

        # Initialize count array
        count = [0] * maxvalue

        # Store the count of each elements in count array
        for i in range(0, size):
            count[self.timeWaiting[i]] += 1

        # Store the cummulative count
        for i in range(1, 10):
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
        size = len(self.timeWaiting)
        maxvalue = max(self.typeOrder)
        timeOrder = [0] * size
        lineOrder = [0] * size
        typeOrder = [0] * size

        # Initialize count array
        count = [0] * maxvalue

        # Store the count of each elements in count array
        for i in range(0, size):
            count[self.typeOrder[i]] += 1

        # Store the cummulative count
        for i in range(1, count):
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
        

    
    def __calcWait(self, ticketId):
        selectedTicket = Ticket.objects.filter(id=ticketId).values().first()
        timeInWaiting = self.__actualTime() - self.__timeToInt(selectedTicket["arrivalDate"],selectedTicket["arrivalTime"])
        return timeInWaiting
    
    def __actualTime(self):
        time = datetime.now()
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
    
    
    
