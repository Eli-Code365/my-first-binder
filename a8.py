#Robert Johnson,Eli Cohen,Tony Rojas
#Python Programming - Assignment 8
#07/23/21

import sys             
import math              

class Shape():
    def __init__(self, label, parameters):
    
        is_shape = True
        
        if label == "Triangle":
            if parameters[0] + parameters[1] < parameters[2]:
                is_shape = False
                
        elif label == "Rectangle" or label == "Square":
            if parameters[0] * parameters[1] <= 0:
                is_shape = False
                
        elif label == "Pentagon" or label == "Hexagon" or label == "Circle":
            if parameters[0] <= 0:
                is_shape = False
                
        if not is_shape:
            print("Not a shape.")
            sys.exit()
            
        self.label = label
        
class Circle(Shape): 
    def __init__(self, radius):
        super().__init__("Circle",[radius])   
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius 
    
    def area(self):
        return math.pi * self.radius**2                

        
class Polygon(Shape):
    
    def __init__(self, label, parameters):
        super().__init__(label, parameters)     
    
    def perimeter(self): #computes perimeter of python
        perimeter_number = 0
        if self.label == "Triangle":
            perimeter_number = self.side_1 + self.side_2 + self.side_3
            
        elif self.label == "Rectangle" or self.label == "Square":
            perimeter_number = 2 * (self.length+self.width)
            
        elif self.label == "Pentagon": 
            perimeter_number = 5 * self.length 
            
        elif self.label == "Hexagon":
            perimeter_number = 6 * self.length
            
        return perimeter_number
         
    def area(self): #computes area of polygon
        area_number = 0
        if self.label == "Triangle":
            s = 0.5 * (self.side_1 + self.side_2 + self.side_3) 
            area_number = math.sqrt(s * (s-self.side_1) * (s-self.side_2) * (s-self.side_3))
        
        elif self.label == "Rectangle" or self.label == "Square":
            area_number = self.length * self.width
            
        elif self.label == "Pentagon": 
            area_number = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.length**2
            
        elif self.label == "Hexagon":
            area_number = 1.5 * math.sqrt(3) * self.length**2
            
        return area_number
        
class Triangle(Polygon):
    def __init__(self, side_1, side_2, side_3):
        super().__init__("Triangle", [side_1,side_2,side_3])  
        self.side_1 = side_1 
        self.side_2 = side_2 
        self.side_3 = side_3 
        
class Rectangle(Polygon):
    def __init__(self, length, width):
        
        if length == width:
            super().__init__("Square", [length, width])  
        else:
            super().__init__("Rectangle", [length, width])  
            
        self.length = length 
        self.width = width 
        
class Pentagon(Polygon):
    def __init__(self, length):
        super().__init__("Pentagon", [length])          
        self.length = length 
        
class Hexagon(Polygon):
    def __init__(self, length):
        super().__init__("Hexagon", [length])             
        self.length = length 


my_circle = Circle(2) #creates a circle
my_triangle = Triangle(3, 7, 4.6) #creates a triangle
my_rectangle = Rectangle(3, 4.5) #creates a rectangle
my_pentagon = Pentagon(3) #creates a pentagon
my_hexagon = Hexagon(3) #creates a hexagon

#prints the perimeter and area of each shape
print(my_circle.area())
print(my_circle.perimeter())
print(my_triangle.area())
print(my_triangle.perimeter())
print(my_rectangle.area())
print(my_rectangle.perimeter())
print(my_pentagon.area())
print(my_pentagon.perimeter())
print(my_hexagon.area())
print(my_hexagon.perimeter())        