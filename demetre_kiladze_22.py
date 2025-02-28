class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
    
    def __str__(self):
        return f"Person(name={self.name}, deposit={self.deposit}, loan={self.loan})"
    
    def buy_house(self, house):
        if house.status == "გასაყიდი" and self.deposit >= house.price:
            self.deposit -= house.price
            house.owner = self
            house.status = "გაყიდული"
        else:
            print("შეძენა შეუძლებელია")


class House:
    def __init__(self, ID, price, owner=None, status="გასაყიდი"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status
    
    def __str__(self):
        return f"House(ID={self.ID}, price={self.price}, owner={self.owner.name if self.owner else None}, status={self.status})"


person1 = Person("გიორგი", deposit=1500)
person2 = Person("ნინო", deposit=800)

house1 = House(ID=1, price=1200)
house2 = House(ID=2, price=900)

person1.buy_house(house1)
print(person1)
print(house1)