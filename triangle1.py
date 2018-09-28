class Triangle:
  base = 0
  height=0
  hyportenus=0
  
  def __init__(self, base, height, hyportenus):
    self.base = base
    self.height= height
    self.hyportenus= hyportenus
    
  def area (self):
    return 0.5*self.base * self.height 
    
  def perimeter(self):
    return (self.base + self.height + hyportenus)
    
small = Triangle(2,3,4)
large = Triangle(5000,70000,8000)
print("base and height of smaller {} and {}".format(small.base,small.height))
print("smaller area",small.area())
print("larger area",large.area())
    
