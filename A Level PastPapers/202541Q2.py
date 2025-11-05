def ReadData():
    Data=[]
    FileName=input("Enter the filename ")
    try:
        File=open(FileName)
        for i in File:
            Data.append(i)
        File.close()
    except:  # noqa: E722
        print("File is not opening ")
        
    return Data

def SplitData(DataArray):
    Red = []
    Green = []
    Blue = []
    Orange = []
    Yellow = []
    Pink = []
    
    for i in DataArray:
        s=i.split(",")
        
        if s[1].strip()=="red":
            Red.append(s[0])
        elif s[1].strip()=="green":
            Green.append(s[0])
        elif s[1].strip()=="blue":
            Blue.append(s[0])
        elif s[1].strip()=="orange":
            Orange.append(s[0])
        elif s[1].strip()=="yellow":
            Yellow.append(s[0])
        else:
            Pink.append(s[0])
    return Red, Green, Blue, Orange, Yellow, Pink        
def StoreData(DataToStore,FileName,):
    
    try:
        File = open(FileName,"a+")
        for i in DataToStore:
            File.write(i)
            File.write("/n")  # "/n"  refer to a new line.
            
        File.close()
    except:  # noqa: E722
        print("Cannot access file. ")
             
x = ReadData()
Red, Green, Blue, Orange, Yellow, Pink = SplitData(x)

StoreData(Red, "Red.txt")
StoreData(Green, "Green.txt")
StoreData(Blue, "Blue.txt")
StoreData(Orange, "Orange.txt")
StoreData(Yellow, "Yellow.txt")
StoreData(Pink, "Pink.txt")
