 #davaleba 1
# a =1
# i = open("data.txt", 'a')
# while a != '0' :
#     a = input("Sheiyvanet informacia- ")
#     if a == '0' :
#         break
#     i.write(a)
#     i.write("\n")
# i.close()

#davaleba 2
# f1= open("data.txt", 'r')
# f2 = open("data2.exe", 'a')
# for  each in f1 :
#     f2.write(each +"  ")
#     f2.seek(1)
# f1.close()
# f2.close()

#davaleba 3
f1 = open("data.txt", 'r')
words=1
xazi=0
symbol = 0
for each in f1 :
    xazi = xazi +1
    for i in range(0, len(each)-1) :
        symbol = symbol+1
        if each[i] == ' ' :
            words = words +1
print("sityvata raodenoba- ", words)
print("simbolota raodenoba- ", symbol)
print("xazzta raodenoba- ", xazi)