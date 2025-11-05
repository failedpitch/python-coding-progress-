# A hospital emergency ward manages patients using a multi-level feedback queue (MLFQ) scheduling 
# system. The system works as follows:

# There are three queues:
# Q1 (highest priority) → patients with life-threatening issues.
# Q2 (medium priority) → patients with serious but not critical conditions.
# Q3 (lowest priority) → patients with minor conditions.
# Patients always enter Q1 first. If a doctor cannot treat them immediately (because all doctors 
# are busy), the patient waits in Q1 for a maximum of T time units.

# If still untreated, they are moved down to Q2.
# If still untreated after another T time units, they are moved down to Q3.
# Doctors always serve patients from the highest non-empty queue, using FIFO order within that 
# queue.

class mlfg:
    def __init__(self):
        self.list_of_patients = []
        
    def enqueue(self, patient_list):
        self.patient_list.append(patient_list)
        
    def mlfg(self):
        return self.patient_list
    
    def dequeue(self):
        if not self.is_empty():
            return self.patient_list.pop(0)
        return("Priority list is empty.")
    
    def is_empty(self):
        return len(self.patient_list) == 0
    
    def display(self):
        return (self.patient_list)
    
class Q1:
    def __init__(self):
        self.high_priority
        
        def enqueue(self, hp):
            self.items.append(hp)
            
        def dequeue(self):
            if not self.is_empty():
                return self.items.pop(0)
            return ("High Priority list is empty.")
        
class Q2:
    def __init__(self):
        self.medium_priority
        
        def enqueue(self, mp):
            self.items.append(mp)
            
        def dequeue(self):
            if not self.is_empty():
                return self.items.pop(0)
            return ("Medium Priority list is empty.")
        
class Q3:
    def __init__(self):
        self.low_priority
        
        def enqueue(self, lp):
            self.items.append(lp)
            
        def dequeue(self):
            if not self.is_empty():
                return self.items.pop(0)
            return ("Low Priority list is empty.")
        
T_time=0
patient_wait = int(input("How long have you waited for?"))
T_time = patient_wait+T_time

if T_time >= 30:
    Q1.append(Q2)
    
elif T_time >= 30+30:
    Q2.append(Q3)
    
else:
    Q1 == Q1 
   
m = mlfg()
m.enqueue("Jeremy")
m.enqueue("Epictatus")
m.enqueue("Jeffery")
m.enqueue("Ellie")

print("Current patient list: ", m.display())
