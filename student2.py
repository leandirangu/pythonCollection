class Student:
  def __init__(self,names,email)
    self.names = names
    self.email = email()
    self.validateName()
    
  def validateEmail(self):
    pass
  
  def validateName(self):
    if type(self.names) is not str:
      raise valueError("{} is not a valid name".format(self.name))
      
jane= Student("Jane".jane)