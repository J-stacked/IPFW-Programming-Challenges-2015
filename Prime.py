print("Enter a number: ")
number=input(" ")
intnumber=int(number)
prime=True
if(intnumber<0):
    intnumber=abs(intnumber)
for x in range(2,intnumber):
    if(intnumber % x == 0):
        if(int(number)>0):
            print(number+" has a factor of "+str(x)+"!")
        if(int(number)<0):
            print(number+" has a factor of "+str(-x)+"!")
        prime=False
if(prime==False):
    print("This is not a prime number!")
else:
    print("This is a prime number!")
