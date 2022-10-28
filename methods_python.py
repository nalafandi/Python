import numpy as np


def randomizing(inp):
    return list(np.random.randint(10, 50, inp))


def summing(lst):
    sum_elements = 0
    for i in lst:
        sum_elements = sum_elements + i
    return sum_elements


while True:
    user_input = int(input('Enter an integer between 5 and 15 for the size of the random series: '))
    if (user_input >= 5) and (user_input <= 15):
        break
    else:
        print('Error... Please try again!')

randomArray = randomizing(user_input)
sumArray = summing(randomArray)

print('The random series = ', randomArray)
print('Sum of random series = ', sumArray)
