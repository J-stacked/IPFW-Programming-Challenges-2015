import math

xSquared=0
ySquared=0  #.... well the squared values of some variables/code later on
zSquared=0

xArray=[]
yArray=[]  #Some arrays to store data
zArray=[]

totalSum=0

for x in range (1,50):  #decently fast algorithm to find the triples
    for y in range (x,50):
        ySquared = (y*y)-(x*x)
        zSquared = 2*x*y
        xSquared = (x*x)+(y*y)  
        if((ySquared*ySquared)+(zSquared*zSquared) == (xSquared*xSquared) and xSquared<=2015 and x<y):
            xArray.append(xSquared)
            yArray.append(ySquared)
            zArray.append(zSquared)
            totalSum+=xSquared+ySquared+zSquared

print("Here are the first 5 triples: ") 
for i in range (0,3):
    print("("+str(xArray[i])+", "+str(yArray[i])+", "+str(zArray[i])+")")

print("Total Sum: " + str(totalSum))
