    #davaleba 1
# numbs = [2,6,21,16,90]
# print(f"jami- {sum(numbs)}")
# print(f"min- {min(numbs)}")
# print(f"max- {max(numbs)}")
# print(f"avarage- {sum(numbs) / len(numbs)}")
# numbs.append(102)
# numbs[2] = 205
# numbs.pop(3)
# numbs.sort()
# print(numbs)

    #davaleba 2
# numbers= []
# for i in range (0,10) :
#     numbers.append(int(input("Sheiyvanet ricxvi- ")))
# print(numbers)

#davaleba 3
nums = [1,3,2,5,6,4,3,9,0]
for i in range (len(nums)-1, -1,-1) :
    if nums[i] % 2 != 0 :
        nums.pop(i)
print(nums)