
dealList=["Apple","Banana"]
userList=["Internet Stalker"]

likeDealList=[0,0]
dislikeDealList=[0,0]

priceDealList=["$0.50","$0.10"]

userID=0

userVoteList=[0,0]

print("addUser() adds new user.")
print("addDeal() adds new deal.")
print("listUsers() lists all users.")
print("listDeals() lists all deals.")

print("Use likeDeal(number) to like a deal.")
print("Use dislikeDeal(number) to dis-like a deal.")

print("Use switchUser(number) to switch to that user.")

def addUser():
    username=input("What is the user's name? ")
    userList.append(username)
    print("Added user: "+str(username))
def addDeal():
    dealname=input("What is the name of the deal? ")
    dealList.append(dealname)
    dealprice=input("What is the price? ")
    priceDealList.append(dealprice)
    likeDealList.append(0)
    dislikeDealList.append(0)
    userVoteList.append(0)
    print("Added deal: "+str(dealname))
def listUsers():
    print("Here are all the users: ")
    print(str(userList[0:]))
def listDeals():
    print("Here are all the deals: ")
    for x in range(0,round(len(dealList))):
        print(str(dealList[x])+": Price "+str(priceDealList[x])+", "+str(likeDealList[x])+" likes, "+str(dislikeDealList[x])+" dislikes")
def likeDeal(number):
    if(userVoteList[number-1]==0):
        likeDealList[number-1]+=1
        print("Liked deal "+str(number))
        userVoteList[number-1]=1
    else:
        print("You already voted on this item!")
    
def dislikeDeal(number):
    if(userVoteList[number-1]==0):
        dislikeDealList[number-1]+=1
        print("disliked deal "+str(number))
        userVoteList[number-1]=1
    else:
        print("You already voted on this item!")
def switchUser(number):
    if(number-1<=len(userList)):
        user=number-1
    else:
        user=len(userList)-1
    for x in range(0,len(userVoteList)-1):
        userVoteList[x]=0
    print("Hello "+str(userList[user]))


while(True):
    try:
        eval(input("Command: "))
    except:
        print("Invalid Command: Try again.")

