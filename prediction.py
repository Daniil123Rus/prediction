from math import sqrt

numbers = input("Enter a list with numbers (sep=' ') > ").split()
elements = int(input("Enter the count of forecasting > "))

data = (numbers, elements)

last = 1
difference_average = []

for n in data[0]:
    n = int(n)
    if last == 0:
        difference_average.append(0)
    else:
        difference_average.append(n / last)
    last = n

last = 1
difference_plus = []

for n in data[0]:
    n = int(n)
    difference_plus.append(n - last)
    last = n

del last

average_multiply = sum(difference_average) / len(data[0])
average_subtract = sum(difference_plus) / len(data[0])

del difference_average, difference_plus

import matplotlib.pyplot as plt

list_average_multiply = []
list_average_subtract = []

for n in range(len(data[0])):
    list_average_multiply.append(data[0][n])
    list_average_subtract.append(data[0][n])

for e in range(data[1]):
    try:
        list_average_multiply.append(sqrt(float(list_average_multiply[-1]) * average_multiply))
    except ValueError:
        list_average_multiply.append(sqrt(-1 * float(list_average_multiply[-1]) * average_multiply))

for e in range(data[1]):
    list_average_subtract.append(float(list_average_subtract[-1]) + average_subtract)

list_average_multiply_subtract = []

for n in range(len(data[0]) + data[1]):
    list_average_multiply_subtract.append((float(list_average_multiply[n]) + float(list_average_subtract[n])) / 2)

plt.plot([i for i in range(len(data[0]))], [float(d) for d in data[0]], '-', [i for i in range(len(data[0]) + data[1])], list_average_multiply_subtract, '--')
plt.show()