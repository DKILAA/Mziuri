import math
class triangle :
    def __init__(self,a,b,c):
        self.a = a 
        self.b  = b
        self.c = c

    def perimeter(self) :
        return self.a + self.b +self.c
    
    def area(self) :
        s = (self.a + self.b +self.c ) / 2
        return math.sqrt(s *(s - self.a) * (s - self.b) * (s - self.c))
    
triangle_1 = triangle (5,6,7)
print ("triangle_1 perimneter ", triangle_1.perimeter())
print ("triangle_1 area ", triangle_1.area())