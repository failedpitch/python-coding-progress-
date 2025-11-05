Queue = [50]
HeadPointer = -1
TailPointer = 0

def Enqueue(StringData):
    global TailPointer
    global HeadPointer
    global Queue
    
    if TailPointer == 50:
        print ("The queue is full. ")
    else:
        StringData.append(Queue)
        TailPointer = TailPointer + 1
        
def Dequeue(Remove):
    global TailPointer
    global HeadPointer
    global Queue
    
    if HeadPointer == -1:
        print ("The queue is empty. ")
    else:
        HeadPointer = HeadPointer + 1
        return (Queue[HeadPointer])
    
def ReadData():
    global TailPointer
    global HeadPointer
    global Queue
    
    file = open("Queue.txt")    
    file.append(Queue)
    file.close()
    
def RecordData(self, ID, Total):   #ID = string  Total = Integer
    self.ID = ID
    self.Total = Total
    
    global TailPointer
    global HeadPointer
    global Queue
    
NumberRecords = 0              #Integer
Records = [NumberRecords]*50   #Integer

def TotalData(self, DataAccessed, Flag):
    
    self.DataAccessed = Dequeue
    self.Flag = False
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total =+ 1
        self.Flag = True
        NumberRecords = NumberRecords + 1
    else:
        for x in range (0, NumberRecords -1):
            if Records[x].ID == DataAccessed:
                Records[x].Total = Records[x].Total + 1
            
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total =+ 1
        NumberRecords = NumberRecords + 1
        
def OutputRecords(self, ID, Total):
    print ("ID ", self.ID, "Total ", self.Total)
    
ReadData()
TotalData()
OutputRecords()    