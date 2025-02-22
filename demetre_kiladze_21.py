    #davaleba 1

# class Cat:
#     def eat(self):
#         print("Cat eats a milk")
    
#     def talk(self):
#         print("Cat says miaww")
    
#     def walk(self):
#         print("Cat can run 20km/h")

# class Dog:
#     def eat(self):
#         print("Dog eats a bone")
    
#     def talk(self):
#         print("Dog says Aww")
    
#     def walk(self):
#         print("Dog can run 40km/h")


# cat = Cat()
# dog = Dog()

# animals = (cat, dog)
# methods = ("eat", "talk", "walk")

# for animal in animals:
#     for method in methods:
#         getattr(animal, method)()
#     print()

    #davaleba 2
# class Currency :
#     def __init__(self,value,unit):
#         self.value = value
#         self.unit = unit

#     def __str__(self):
#         return f"{float(self.value)} {self.unit}"
    
#     def changeTo(self, currency) :
#         if currency == "USD" and self.unit == "GEL" :
#             return self.unit * 0.35
#         elif currency == "USD" and self.unit == "EUR" :
#             return self.unit * 1.05
#         elif currency == "GEL" and self.unit == "USD" :
#             return self.unit * 2.82
#         elif currency == "GEL" and self.unit == "EUR" :
#             return self.unit * 2.96
#         elif currency == "EUR" and self.unit == "USD" :
#             return self.unit * 0.96
#         else : 
#             return self.unit *  2.96