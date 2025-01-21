class Student:
    def __init__(self, first_name, last_name, personal_id, birth_year, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.personal_id = personal_id
        self.birth_year = birth_year
        self.grades = grades

    def __str__(self):
        return (
            f"Student:: {self.first_name} {self.last_name}\n"
            f"Personal ID: {self.personal_id}\n"
            f" Birth Year: {self.birth_year}\n"
            f"Grades: {self.grades}"
        )

    def years_until_18(self):
        current_year = 2025
        age = current_year - self.birth_year
        if age >= 18:
            return 0
        return 18 - age


student1 = Student(
    first_name="Nana",
    last_name="katamadze",
    personal_id="01012000001",
    birth_year=2010,
    grades={"math": 95, "programming": 100}
)

student2 = Student(
    first_name="Giorgi",
    last_name="Jajanidze",
    personal_id="02022000002",
    birth_year=2008,
    grades={"math": 88, "programming": 90}
)

student3 = Student(
    first_name="Jemala",
    last_name="Kiladze",
    personal_id="03032000003",
    birth_year=2015,
    grades={"math": 100, "programming": 99}
)
print(student1)
print(f"Nana will be 18 in {student1.years_until_18()} years.\n")

print(student2)
print(f"Giorgi will be 18 in  {student2.years_until_18()} years.\n")

print(student3)
print(f"Jemala will be 18 in  {student3.years_until_18()} years.\n")