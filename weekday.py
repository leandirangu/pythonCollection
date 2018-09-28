class Student:
  name = "John Doe"
  weekday = True
  
  def __init__(self,name,weekday):
    self.name = name
    self.weekday = weekday
    
  def morning(self):
    if self.weekday:
      return "wakes up"
    else:
      return "sleeps"
    
    
fatma = Student("Fatma Moha",True)
judith = Student(name="Judith Mueni",weekday=False)
print("Fatma:",fatma.morning())
