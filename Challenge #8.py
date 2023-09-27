InputString1=input("Word #1: ")  #the input string
InputString2=input("Word #2: ")  #the input string
InputString3=input("Word #3: ")  #the input string

anagram1=[]
anagram2=[]
anagram3=[]

def anagrams(word):
    if len(word) < 2:
        return word
    else:
        tmp = []
        for i, letter in enumerate(word):
            for j in anagrams(word[:i]+word[i+1:]):
                foundDupe=False
                for x in range(0,len(tmp)):
                    if(tmp[x]==j+letter):
                        foundDupe=True
                if(foundDupe==False):
                    tmp.append(j+letter)
    tmp.sort()
    return tmp




anagram1=anagrams(InputString1)
anagram2=anagrams(InputString2)
anagram3=anagrams(InputString3)

def printanagram(anagram):
    for i in anagram:
        print(i)
    print("--------")

printanagram(anagram1)
printanagram(anagram2)
printanagram(anagram3)

print("Average number of anagrams: "+str(float((len(anagram1)+len(anagram2)+len(anagram3))/3.0)))
print("Total number of anagrams: "+str(int(len(anagram1)+len(anagram2)+len(anagram3))))
