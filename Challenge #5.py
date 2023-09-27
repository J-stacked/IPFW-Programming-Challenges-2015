import random

productArray=[]


largestColumnRow=input("What should be the maximum value for the rows and columns? ")


columnHeight=round(random.randint(4,int(largestColumnRow)))
rowLength=round(random.randint(4,int(largestColumnRow)))

array1=[]

horizontalMulti=0
verticalMulti=0
row=1
posX=0

for x in range (0,round(columnHeight*rowLength)):
    array1.append(random.randint(1,9))

for x in range (0,round(len(array1))):
    if(x%rowLength==0):
        print(str(array1[x:rowLength+x]))
        productArray.append(array1[x]*array1[x+1]*array1[x+2]*array1[x+3])
        if(rowLength>4):
            horizontalMulti=rowLength-4
            while(horizontalMulti!=0):
                productArray.append(array1[x+horizontalMulti]*array1[x+1+horizontalMulti]*array1[x+2+horizontalMulti]*array1[x+3+horizontalMulti])
                horizontalMulti-=1

for y in range (0,round(len(array1))):
    if(y%rowLength==0 and y!=0):
        row+=1
        posX=0
        print("row")
    if(row<=columnHeight-3):
        if(posX<rowLength-3):
            print("diagonal ["+str(array1[rowLength*(row-1)+posX])+", "+str(array1[rowLength*row+posX+1])+", "+str(array1[rowLength*(row+1)+posX+2])+", "+str(array1[rowLength*(row+2)+posX+3])+"]")
            productArray.append(array1[rowLength*(row-1)+posX]*array1[rowLength*row+posX+1]*array1[rowLength*(row+1)+posX+2]*array1[rowLength*(row+2)+posX+3])
        print("vertical ["+str(array1[rowLength*(row-1)+posX])+", "+str(array1[rowLength*row+posX])+", "+str(array1[rowLength*(row+1)+posX])+", "+str(array1[rowLength*(row+2)+posX])+"]")
        productArray.append(array1[rowLength*(row-1)+posX]*array1[rowLength*row+posX]*array1[rowLength*(row+1)+posX]*array1[rowLength*(row+2)+posX])
        if(posX<rowLength-1):
            posX+=1
    

print("column "+str(columnHeight)+" row "+str(rowLength))

print(str(productArray[0:]))

print("Largest product: "+str(max(productArray)))
