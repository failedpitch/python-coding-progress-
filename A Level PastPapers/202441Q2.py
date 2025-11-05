class Horse:
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self.Name = Name                            #String
        self.MaxFenceHeight = MaxFenceHeight        #Integer
        self.PercentageSuccess = PercentageSuccess  #Char
        
        
    def GetName(self):
        return self.Name
    
    def GetMaxFenceHeight(self):
        return self.MaxFenceHeight
    
    def Success(self, Height, Risk):
        if Height > self.MaxFenceHeight:
            return self.PercentageSuccess * 0.2
        else:
            if Risk == 1:
                return self.PercentageSuccess * 1.0
            elif Risk == 2:
                return self.PercentageSuccess *0.9
            elif Risk == 3:
                return self.PercentageSuccess *0.8
            elif Risk == 4:
                return self.PercentageSuccess *0.7
            else:
                return self.PercentageSuccess *0.6
            
class Fence:
    def __init__ (self, Height, Risk):
        self.Height = Height              #Char
        self.Risk = Risk                  #Integer
    
    def GetHeight(self):
        return self.Height
    
    def GetRisk(self):
        return self.Risk
    
Course = []
for x in range(0, 4):
    Valid = False
    while Valid == False:
        Height = int(input("Enter the height in cm"))
        if(Height >= 70 and Height <= 180):
            Valid = True
    Valid = False
    while Valid == False:
        Risk = int(input("Enter the risk between 1 (easy) and 5 (hard)"))
        if(Risk >= 1 and Risk <= 5):
            Valid = True
            Course.append(Fence(Height, Risk))

Horses = []
Horses.append (Horse("Beauty ", 150, 72))    
Horses.append (Horse("Jet ", 160, 65))

AverageSuccess = []
for y in range(0, 2):
    Total = 0
    for x in range(0, 4):
        Chance = Horses[y].Success(Course[x].GetHeight(), Course[x].GetRisk())
        print(Horses[y].GetName(), "Fence", x + 1, "Chance of success is", Chance, "%")
        Total = Total + Chance
    Average = Total / 4
    AverageSuccess.append(Average)
    print(Horses[y].GetName(), "average success rate is", Average, "%")        
    
Highest = AverageSuccess[0]
Winner = 0
for x in range(1, 2):
    if Highest < AverageSuccess[x]:
        Winner = x
        Highest = AverageSuccess[x]
print(Horses[Winner].GetName(), "has the highest average chance of success")

print (Horses)