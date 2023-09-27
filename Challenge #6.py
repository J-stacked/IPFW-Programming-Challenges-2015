#to store the MSLCM sets
MSLCM=0
#temporary array used to store 1 lcm set
LCMArray=[]

startN=2
endN=2016

for x in range (startN,endN+1):
    for y in range(1,x+1):
        if(x%y==0):
            LCMArray.append(y)
            MSLCM+=y

    print(str(x)+" "+str(LCMArray[0:]))
    
    LCMArray=[]
print()
print("The MSLCM total is: "+str(MSLCM))


