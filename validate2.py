class Rectangle:
  length =20
  width=10
  
  def __init__(self, length, width):
    self.length = length
    self.width=width
    self.ValidateDimension()
    
    
  def ValidateDimension(self):
    self.width = float(self.width)
    self
    if (self.width.isNumeric() and self.length.isNumeric) ==False
      raise ValueError("parameter is not numeric")
      
 
    
  def area (self):
    return self.length * self.width
    
  def perimeter(self):
    return 2*(self.length + self.width)
    
small = Rectangle(2,3)
invalid = Rectangle(2,5)
print(invalid.area())