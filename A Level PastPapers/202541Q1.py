Queue = [-1] * 20
HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueue(InputData):
    global Queue
    global HeadPointer
    global TailPointer
    global NumberItems
    
    if NumberItems>=20:
        return False
    
    if TailPointer <= -1:
        TailPointer = 0
        HeadPointer = 0
        Queue[TailPointer] = InputData
        
    else:
        TailPointer = TailPointer + 1
        
        if TailPointer == 20:
            TailPointer = 0
            
        Queue[TailPointer] = InputData
    NumberItems = NumberItems + 1    
    return True

for i in range(1,26):
    if Enqueue(i): 
        print (i," Successful")
    else:
        print (i," Unsuccessful")
        
def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    global NumberItems
    
    if NumberItems <= 0:
        return -1
    else:
        x = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1
        if HeadPointer >= 20:
            HeadPointer = 0
        NumberItems = -1
        if NumberItems == 0:
            HeadPointer = -1
            TailPointer = -1
            
        return x
    
y=Dequeue()
print(y)
y=Dequeue()
print(y)