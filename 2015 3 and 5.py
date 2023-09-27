number3=0
number5=0
number35=0
for x in range (1,16):
    if(x%3==0):
        number3+=x
    if(x%5==0):
        number5+=x
    if(x%3==0 and x%5==0):
        number35+=x

print("Sum of numbers divisible by 3: "+str(number3))
print("Sum of numbers divisible by 5: "+str(number5))
print("Sum of numbers divisible by 3 or 5: "+str(number3+number5))
print("Sum of numbers divisible by 3 and 5: "+str(number35))

