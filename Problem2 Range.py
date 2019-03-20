#Julissa Franc0
#02/28/2019
#Problem 2 Check whether a number is in a given range

def inRange(number):
    if number in range(1, 10):
        print("Number is withint range")
    else:
        print("Number is outside of range")
inRange(1)
inRange(15)
inRange(5)
