#davaleba 1
# class People :
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def get_email(self) :
#         return f"{self.firstname}.{self.lastname}.school@mziuri.ge"
    
# class Student(people) :
#     def get_email(self) :
#         return f"{self.firstname}.{self.lastname}@1mziuri.ge"
    
# class Lecturer(people) :
#     def get_email(self) :
#         return f"{self.firstname}.{self.lastname}@1mziuri.ge"

# p1 = people("jemali", "Malatsidze")
# p2 = people ("Levani", "Jajanidze")
# p3 = people("Mari", "Abashidze")

# print("jemala's email: ", p1.get_email())
# print("Mari's email: ", p3.get_email())

      #davaleba 2
# class LybraryItem :
#     def __init__(self,title,subject,status):
#         self.title = title
#         self.subject = subject
#         self.status = status
    
#     def booking(self) :
#         if self.status == "occupied" :
#             return "Didnt Booked"
#         else :
#             return "Booked"
        
# class Book(lybraryItem) :
#     def __init__(self, title, subject, status, ISBN, authors):
#         super().__init__(title, subject, status)
#         self.ISBN = ISBN
#         self.authors = authors

# class Magazine(lybraryItem) :
#      def __init__(self, status,journalName, volume):
#         super().__init__("Dino", "information", "available" )
#         self.journalName = journalName
#         self.volume = volume

# class CD(lybraryItem) :
#     def __init__(self,title):
#         self.title = title

#     def booking() :
#         return "You can't book CD"

# p1 = lybraryItem("Programing_PY","Python","occupied")
# p2 = CD("Zangi Work")
# p3= Magazine("available","Nigger Journal", "69+")

# print (p3.booking())
# print (p1.booking())

    #davaleba 3
class Contacts:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class MailSender:
    def send_mail(self):
        print("Your mail sent to:", self.email)

class Friends(Contacts, MailSender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email

class Family(Contacts, MailSender):
    def __init__(self, name, phone, email, birthday):
        super().__init__(name, phone)
        self.email = email
        self.birthday = birthday

p1 = Friends("Jemala", "591-991-991", "JemalaTyemala@gmail.com")
p2 = Family("Vano", "555-555-555", "VanoVano19@gmail.com", "29/02/2000")

p1.send_mail()
p2.send_mail()


    #davaleba 4