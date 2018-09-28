class Student:
  name = "John Doe"
  def __init__(self,name):
    self.name = name
    
  def get_name(self):
    return self.name
    
  def welcome(self):
    return "welcome {} to Akirachix".format(self.name)
    
fatma = Student("Fatma Moha")
judith = Student("Judith Mueni")
#print(fatma.welcome())
print(judith.welcome())