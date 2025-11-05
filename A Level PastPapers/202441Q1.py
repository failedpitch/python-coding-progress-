def ReadData():
    stringdata = [] 
    try:
       file = open ("Data.txt")
       for i in file:
           file.strip(i) 
           file.append(stringdata)
           return stringdata
    except:  # noqa: E722
        print ("Unable to access file. ")   
        
def FormatArray(DataArray):
    OutputText = ""
    for x in range(0, 45):
        OutputText = OutputText + DataArray[x] + " "
    return OutputText

def CompareStrings(First, Second):
    Count = 0
    while True:
        if First[Count] < Second[Count]:
            return 1
        elif First[Count] > Second[Count]:
            return 2
        else:
            Count = Count + 1
            
def Bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            result = CompareStrings(arr[j], arr[j + 1])
            if result == 2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = ReadData()           
x = Bubble(arr)
print (FormatArray(x))
