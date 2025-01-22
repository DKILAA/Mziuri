class Student:
    def __init__(self, name, lastname, personal_id, birth_year, grades):
        self.name = name
        self.lastname = lastname
        self.personal_id = personal_id
        self.birth_year = birth_year
        self.grades = grades

    def __str__(self):
        return f"name : {self.name } ,\n lastname : {self.lastname},\n personal_id : {self.personal_id} \n birth_year: {self.birth_year}\n grades: {self.grades}"

    def years_until_18(self):
        current_year = 2025
        age = current_year - self.birth_year
        if age >= 18:
            return "*Already was!*"
        return 18 - age

student1 = Student("nana", "varlamishvili" ,"0121312" , 2008, {"math": 95, "programming": 100})
student2 = Student("jemala", "zangidze" ,"3562234" , 2003 , {"math": 0, "programming": 101})
student3 = Student("nugzari", "pavlovic" ,"777217" , 2009 , {"math": 0, "programming": 0})

print(student1, "\n")
print(f"will be 18 in {student1.years_until_18()} years")

print(student2,"\n" )
print(f"Giorgi will be 18 in  {student2.years_until_18()} years")

print(student3, "\n")
print(f"Jemala will be 18 in  {student3.years_until_18()} years")