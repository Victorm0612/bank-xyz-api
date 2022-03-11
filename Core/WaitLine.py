from asyncio.windows_events import NULL
from datetime import datetime
from Core.models import Service

class WaitLine():

    line = []
    timeWaiting = []
    typeOrder = []

    def __init__(self, clientId, timeArrival, serviceId):
        self.line.append(clientId)
        self.timeWaiting.append(self.calcWait(timeArrival))
        self.typeOrder.append(getType(serviceId))

    def addClientToLine(self,clientId, timeArrival, serviceId):
        self.line.append(clientId)
        self.timeWaiting.append(self.calcWait(timeArrival))
        self.typeOrder.append(getType(serviceId))

        self.sortBytimeWaiting()
        self.sortByTypeOrder()

    def getNextTurn(self,typeTeller):

        nextTurn = NULL
        for i in range(len(self.typeOrder)):
            if self.typeOrder[i] == typeTeller:
              nextTurn = self.line[i]
              self.eraseTurnFromLine(nextTurn)

        if nextTurn == NULL:
            nextTurn = self.line[0]
            self.eraseTurnFromLine(nextTurn)
        
        return nextTurn

    def eraseTurnFromLine(self, turn):
        for i in range(len(self.line)):
            if self.line[i] == turn:
                self.line.pop(i)
                self.timeWaiting.pop(i)
                self.typeOrder.pop(i)

    
    def sortBytimeWaiting(self):

        # The output character array that will have sorted arr
        outputTime = [0 for i in range(len(self.timeWaiting))]
        outputId = self.line
        
        # Create a count array to store count of individual
        # characters and initialize count array as 0
        count = [0 for i in range(256)]
    
        # Store count of each character
        for i in self.timeWaiting:
            count[ord(i)] += 1
    
        # Change count[i] so that count[i] now contains actual
        # position of this character in output array
        for i in range(256):
            count[i] += count[i-1]
    
        # Build the output character array
        for i in range(len(self.timeWaiting)):
            outputTime[count[ord(self.timeWaiting[i])]-1] = self.timeWaiting[i]
            outputId[count[ord(self.timeWaiting[i])]-1] = self.line[i]
            count[ord(self.timeWaiting[i])] -= 1
    
        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(len(self.timeWaiting)):
            self.timeWaiting[i] = outputTime[i]
            self.line[i] = outputId[i]

    def sortByTypeOrder(self):

        # The output character array that will have sorted arr
        outputType = [0 for i in range(len(self.typeOrder))]
        outputId = self.line
        
        # Create a count array to store count of individual
        # characters and initialize count array as 0
        count = [0 for i in range(256)]
    
        # Store count of each character
        for i in self.typeOrder:
            count[ord(i)] += 1
    
        # Change count[i] so that count[i] now contains actual
        # position of this character in output array
        for i in range(256):
            count[i] += count[i-1]
    
        # Build the output character array
        for i in range(len(self.typeOrder)):
            outputType[count[ord(self.typeOrder[i])]-1] = self.typeOrder[i]
            outputId[count[ord(self.typeOrder[i])]-1] = self.line[i]
            count[ord(self.typeOrder[i])] -= 1
    
        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(len(self.typeOrder)):
            self.typeOrder[i] = outputType[i]
            self.line[i] = outputId[i]
        

    
    def calcWait(self, timeArrival):
        timeInWaiting = self.actualTime() - self.timeToInt(timeArrival)
        return timeInWaiting
    
    def actualTime():
        time = datetime.now()
        intTime = time.year * 100000 + time.month * 10000 + time.day * 1000 + time.hour * 100 + time.minute * 10 + time.second
        return intTime

    def timeToInt(self, time):
        yyyy, mn, dy, hh, mm , ss = map(int, time.split(':'))
        intTime = yyyy * 100000 + mn * 10000 + dy * 1000 + hh * 100 + mm * 10 + ss
        return intTime
    
    def getType(self, serviceId):
        ServiceToSearch = Service.objects.filter(service_id=serviceId).values().first()
        return ServiceToSearch["serviceType"]
