class Rectangle :
    def __init__(self,color,width,length):
        self.color = color
        self.width = width
        self.length = length

    def __str__(self):
        return f"color = {self.color} width = {self.width} length = {self.length}"
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    
    def area(self) :
        return self.width * self.length
    
obj_1 = Rectangle("blue", 3 , 6)
obj_2 = Rectangle("red", 2 , 3)
obj_3 = Rectangle("orange", 4 , 7)
print(f"object_1 Area=  {obj_1.area()}")