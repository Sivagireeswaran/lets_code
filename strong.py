import math
a=int(input("no"))
copy = a
curr=0
while a:
    rem = a%10
    
    curr += math.factorial(rem)
    
    a = a // 10
if curr == copy:
    print("strong")
else:
    print("NS")
