#declaring variables
previousTerm=1
currentTerm=2
SumOfTerms=0
evenNumbers=1
finished=False
countTo=0
SumOfEven=2
#a small issue, but by printing these, I am "fixing" it
print("1")
print("2")
print("Even: "+str(evenNumbers))
#while it is not finished counting and adding numbers
while(finished==False):
    SumOfTerms=currentTerm+previousTerm
    previousTerm=currentTerm
    currentTerm=SumOfTerms
    #displays the first 100 numbers
    if(countTo<100):
        countTo+=1
        print(str(SumOfTerms))
    #checks if the current number is evenly divisible by 2
    if(SumOfTerms%2==0):
        evenNumbers+=1
        print("Even: "+str(evenNumbers))
        SumOfEven+=SumOfTerms
    #if it has gotten to 2015 even numbers
    if(evenNumbers==2015):
        print("Done!")
        finished=True
#printing the sum of the digits in the sum of even numbers
print(str(sum(map(int, str(SumOfEven))))+" is the sum of the digits in the sum of the even numbers")
