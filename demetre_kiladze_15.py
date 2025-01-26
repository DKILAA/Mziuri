    #davaleba 1
# def divide(a,b) :
#     try :
#        return(a/b)
#     except :
#         return ("0 -ze gayofa ar sheidzleba!")
# print(divide(6,0))

#davaleba 2
# text = "BARCA"
# try :
#     print(text[9])
# except IndexError :
#     print("IndexError !")

#davaleba 3
try :
    f = open("myresult.txt", 'r')
except FileNotFoundError :
    print("Faili ver moidzebna!")
finally :
    f.close()