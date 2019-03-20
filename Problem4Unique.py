#Julissa Franco
#02.28.2019

#Function recieves list and prints out only the unique elements

def uniqueList(numbers):
    newList=[]
    for n in numbers:
        if n not in newList:
            newList.append(n)
    return newList

print(uniqueList([1, 2,2,3,3,3,7,4,3,10]))
