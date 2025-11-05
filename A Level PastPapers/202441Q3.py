LinkedList = []
FirstNode = -1
FirstEmpty = 0

for x in range(0, 19):
    LinkedList.append([-1, x + 1])
LinkedList.append([-1, -1])

def InsertData():
    global LinkedList
    global FirstNode
    global FirstEmpty
    
    for i in range(5):
        if FirstEmpty == -1:
            break
        NextEmpty = LinkedList[FirstEmpty][1]
        LinkedList[FirstEmpty][0] = int(input("Enter the next number: "))
        LinkedList[FirstEmpty][1] = FirstNode
        FirstNode = FirstEmpty
        FirstEmpty = NextEmpty

def OutputLinkedList():
    global LinkedList
    global FirstNode
    
    CurrentPointer = FirstNode
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]

def RemoveData(ItemToRemove):
    global LinkedList
    global FirstNode
    global FirstEmpty
    
    if LinkedList[FirstNode][0] == ItemToRemove:
        NewFirst = LinkedList[FirstNode][1]
        LinkedList[FirstNode][1] = FirstEmpty
        FirstEmpty = FirstNode
        FirstNode = NewFirst
    else:
        CurrentPointer = FirstNode
        PreviousNode = -1
        while CurrentPointer != -1 and LinkedList[CurrentPointer][0] != ItemToRemove:
            PreviousNode = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer][1]
        
        if CurrentPointer != -1 and LinkedList[CurrentPointer][0] == ItemToRemove:
            LinkedList[PreviousNode][1] = LinkedList[CurrentPointer][1]
            LinkedList[CurrentPointer][0] = -1
            LinkedList[CurrentPointer][1] = FirstEmpty
            FirstEmpty = CurrentPointer

InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()
            
    