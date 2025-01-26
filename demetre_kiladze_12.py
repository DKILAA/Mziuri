#davaleba 1
# txt= 'w3resource'
# d = {}
# l=1
# for i in range(0,len(txt) -1) :
#     for j in range(i +1,len(txt)) :
#        if  txt[i] == txt[j] :
#           l+= 1
#     if txt[i] not in d: 
#         d[txt[i]] = l
#     l=1
# print(d)

#davaleba 2
d = {'Math':81, 'Physics':83, 'Chemistry':87}
d1=d.keys()
print(d1)
d1 = sorted(d.values(),reverse=True)
print(d1)
