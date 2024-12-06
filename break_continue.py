#break
i = 1
while i <= 5 :
    print(1)
    if(i == 3):
        break
    i += 1

print("end of loop")    

nums = (1, 4, 16, 25, 36, 49, 61, 75, 81, 100)
x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding..")
        i += 1

print("end of loop")     

#continiue
i = 1
while i <= 5 :
    print(1)
    if(i == 3):
        continue
    i += 1

print("end of loop")  