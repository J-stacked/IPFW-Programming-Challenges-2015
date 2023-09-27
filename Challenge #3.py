import math
finalNumber=0
tempNumber=1

for x in range (1,2016):
    finalNumber+=math.factorial(x)
    tempNumber+=1
print(str(sum(map(int, str(finalNumber))))+" is the sum")
