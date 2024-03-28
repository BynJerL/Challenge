# There's empty number between 0 and 6, 0 not included
# This is the algorithm for adding 1, 2, 3, and 5
# If exceeding the range, the program will add the next number (in this case: 7, 8, and 9)
example = [6,4]

def foo():
    global example
    tempNumber = 1
    numbers = example
    numbers.sort()
    
    for number in numbers:
        if number != tempNumber:
            break
        else:
            tempNumber += 1
    
    print(tempNumber)
    example.append(tempNumber)

for x in range(0,7):
    foo()