import pandas as d


input = int(input('Enter any integer greater than 0: '))

if input > 0:
    print('You entered ', input)
    even = []
    odd = []
    fibo = []
    for i in range(input):
        even.append(i * 2)
        odd.append(even[i] + 1)
        if i == 0:
            fibo.append(0)
        if i == 1:
            fibo.append(1)
        if i > 1:
            fibo.append(fibo[i - 2] + fibo[i - 1])

    results = d.DataFrame({'Even': even, 'Odd': odd, 'Fibonacci': fibo})

    print(results)

elif input == 0:
    print('Please enter an integer that is greater than 0!')
