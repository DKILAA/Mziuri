import math
class triangle :
    def __init__(self,a,b,c):
        self.__a = a 
        self.__b  = b
        self.__c = c

    def perimeter(self) :
        return self.__a + self.__b +self.__c
    
    def area(self) :
        s = (self.__a + self.__b +self.__c ) / 2
        return math.sqrt(s *(s - self.__a) * (s - self.__b) * (s - self.__c))
    
triangle_1 = triangle (5,6,7)
print ("triangle_1 perimneter ", triangle_1.perimeter())
print ("triangle_1 area ", triangle_1.area())