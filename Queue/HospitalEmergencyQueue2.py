class MLFQ:
    def __init__(self):
        self.patient_list = []
        
    def enqueue(self, patient):
        self.patient_list = self.patient_list + [patient]
        
    def dequeue(self):
        if not self.is_empty():
            patient = self.patient_list[0]
            self.patient_list = self.patient_list[1:]
            return patient
        return "Priority list is empty."
    
    def is_empty(self):
        return len(self.patient_list) == 0
    
    def display(self):
        return self.patient_list
    

class Q1:
    def __init__(self):
        self.items = []
        
    def enqueue(self, hp):
        self.items = self.items + [hp]
            
    def dequeue(self):
        if not self.is_empty():
            patient = self.items[0]
            self.items = self.items[1:]
            return patient
        return "High Priority list is empty."
    
    def is_empty(self):
        return len(self.items) == 0


class Q2:
    def __init__(self):
        self.items = []
        
    def enqueue(self, mp):
        self.items = self.items + [mp]
            
    def dequeue(self):
        if not self.is_empty():
            patient = self.items[0]
            self.items = self.items[1:]
            return patient
        return "Medium Priority list is empty."
    
    def is_empty(self):
        return len(self.items) == 0


class Q3:
    def __init__(self):
        self.items = []
        
    def enqueue(self, lp):
        self.items = self.items + [lp]
            
    def dequeue(self):
        if not self.is_empty():
            patient = self.items[0]
            self.items = self.items[1:]
            return patient
        return "Low Priority list is empty."
    
    def is_empty(self):
        return len(self.items) == 0


T = 3
time = 0
q1 = Q1()
q2 = Q2()
q3 = Q3()
mlfq = MLFQ()

mlfq.enqueue({"id": "Swarnava", "arrival": time})
mlfq.enqueue({"id": "June", "arrival": time})
mlfq.enqueue({"id": "Jeffery", "arrival": time})
mlfq.enqueue({"id": "Elanore", "arrival": time})
mlfq.enqueue({"id": "Ellie", "arrival": time})
mlfq.enqueue({"id": "Debbie", "arrival": time})
mlfq.enqueue({"id": "Shawn", "arrival": time})
mlfq.enqueue({"id": "Flou", "arrival": time})
mlfq.enqueue({"id": "Sean", "arrival": time})
mlfq.enqueue({"id": "Gertrude", "arrival": time})
mlfq.enqueue({"id": "Gemma", "arrival": time})

while not mlfq.is_empty():
    patient = mlfq.dequeue()
    q1.enqueue(patient)

for t in range(6):
    print("\nTime:", t)
    
    if not q1.is_empty():
        patient = q1.dequeue()
        print("Doctor treating from Q1:", patient["id"])
    elif not q2.is_empty():
        patient = q2.dequeue()
        print("Doctor treating from Q2:", patient["id"])
    elif not q3.is_empty():
        patient = q3.dequeue()
        print("Doctor treating from Q3:", patient["id"])
    else:
        print("No patients waiting")
    
    temp_q1 = []
    for p in q1.items:
        if t - p["arrival"] >= T:
            p["arrival"] = t
            q2.enqueue(p)
        else:
            temp_q1 = temp_q1 + [p]
    q1.items = temp_q1
    
    temp_q2 = []
    for p in q2.items:
        if t - p["arrival"] >= T:
            p["arrival"] = t
            q3.enqueue(p)
        else:
            temp_q2 = temp_q2 + [p]
    q2.items = temp_q2
    
    print("Q1:", [p["id"] for p in q1.items])
    print("Q2:", [p["id"] for p in q2.items])
    print("Q3:", [p["id"] for p in q3.items])