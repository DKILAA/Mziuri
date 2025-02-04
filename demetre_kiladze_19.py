
class animal :
    def __init__(self, name,color):
        self.name = name
        self.color = color

    def say_hi(self) :
        print (f"Hello my name is {self.name} with color {self.color} and i am an animal")

class dog(animal) :
    def say_hi(self) :
      print (f"Hello my name is {self.name} with color {self.color} and i am a Dog")

animal_1 = dog("Jemala" , "zangi" )
animal_1.say_hi()