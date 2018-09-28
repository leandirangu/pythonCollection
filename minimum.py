class TaxPayer:
  income = 0
  def __init__(self,name,income,minimum):
    self.income = income
    self.name = name
    self.ValidateIncome()
    self.validateName()
    self.ValidateMinimum()
    
  def ValidateIncome(self):
    if self.income<=10000: 
      raise ValueError("The income {} is minimum".format(self.income))
      
  def validateName(self):
    if self.income.isminimum() == False:
      raise ValueError("The minimum {} is less than 10000".format(self.income))
      
  def calculate_tax(self):
    return float(self.income) * 0.3
      
    
    
income = input("what is your income:")
name=input("what is your name:")
minimum=input("what is your minimum:")
employee = TaxPayer(name,income,minimum)
print(employee.calculate_tax())