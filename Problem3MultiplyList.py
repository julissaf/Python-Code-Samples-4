# Julissa Franco
# 02.29.2019
# Function will multuply numbers in a list

def multiplyList(numbers):
    total = 1
    for n in numbers:
        total *= n
#      total=total * n
    return (total)

n=[1,5,3,-8,10]

print(multiplyList(n))

print(multiplyList([1,2,3]))
