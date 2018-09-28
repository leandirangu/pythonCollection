class Circle:
  radius =0 
  diameter= 0
  
  def __init__(self,radius, diameter):
    self.radius = radius
    self.diameter= diameter
    
  def area (self):
    return 3.14*(self.radius* self.radius) 
    
  def perimeter(self):
    return (2 * 3.14 * self.radius)
    
small = Circle(5,10)
large = Circle(25,50)
print("radius and diameter of smaller {} and {}".format(small.radius, small.diameter))
print("smaller area",small.area())
print("larger area",large.area())
print("radius and diameter of bigger {} and {}".format(small.radius,small.diameter))
print("smaller perimeter",small.perimeter())
print("larger perimeter",large.perimeter())