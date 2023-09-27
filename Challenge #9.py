primes=[]

def noDuplicates(array):
    if(len(array) == len(set(array))):
        return True
    else:
        return False

def primer(n):

    primes=[]
    
    for x in range(2,n+1):
        
        prime=True
        
        for i in range(2,x+1):
            if(x % i == 0 and i!=x):
                prime=False
                
        if(prime==True):
            primes.append(x)
    #done generating primes
    #print(primes)
    print("Prime sums")
    #now to generate sets of prime sums
    tmp=[]
    output=[]
    #one number
    for x in range(0,len(primes)):
        if(primes[x]==n):
            tmp=[]
            tmp.append(primes[x])
            print(tmp)
    #two numbers
    for x in range(0,len(primes)):
        for y in range(0,round(len(primes)/2)):
            if(primes[x]+primes[y]==n):
                tmp=[]
                tmp.append(primes[x])
                tmp.append(primes[y])
                tmp.sort()
                if(tmp not in output and noDuplicates(tmp)):
                    output.append((tmp))
                    print(tmp)
    #three numbers
    for x in range(0,len(primes)):
        for y in range(0,len(primes)):
            for z in range(0,round(len(primes)/2)):
                if(primes[x]+primes[y]+primes[z]==n):
                    tmp=[]
                    tmp.append(primes[x])
                    tmp.append(primes[y])
                    tmp.append(primes[z])
                    tmp.sort()
                    if(tmp not in output and noDuplicates(tmp)):
                        output.append((tmp))
                        print(tmp)
    #four numbers!?!?!??!
    for x in range(0,len(primes)):
        for y in range(0,len(primes)):
            for z in range(0,len(primes)):
                for i in range(0,round(len(primes)/2)):
                    if(primes[x]+primes[y]+primes[z]+primes[i]==n):
                        tmp=[]
                        tmp.append(primes[x])
                        tmp.append(primes[y])
                        tmp.append(primes[z])
                        tmp.append(primes[i])
                        tmp.sort()
                        if(tmp not in output and noDuplicates(tmp)):
                            output.append((tmp))
                            print(tmp)
    #five numbers!
    for x in range(0,len(primes)):
        for y in range(0,len(primes)):
            for z in range(0,len(primes)):
                for i in range(0,len(primes)):
                    for j in range(0,round(len(primes)/2)):
                        if(primes[x]+primes[y]+primes[z]+primes[i]+primes[j]==n):
                            tmp=[]
                            tmp.append(primes[x])
                            tmp.append(primes[y])
                            tmp.append(primes[z])
                            tmp.append(primes[i])
                            tmp.append(primes[j])
                            tmp.sort()
                            if(tmp not in output and noDuplicates(tmp)):
                                output.append((tmp))
                                print(tmp)
   

number=input("Number: ")

primer(int(number))
