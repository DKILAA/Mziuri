    #davaleba 1
import random
nums = []
for i in range (0,10) :
    nums.append(random.randint(25,110))

print(nums)
print(min(nums))

    #davaleba 2
def function(s1,s2) :
    for i in s1 :
        for j in s2 :
            if i == j:
                return True
                break
    return False
s1 = [1,3,2,5,6]
s2 = [0,11,42,33]
print(function(s1,s2))
