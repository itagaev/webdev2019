import math

def powerDeg(a, b):
    return a ** b

numbers = [float (x) for x in input().split()]

x = numbers[0]
y = numbers[1]

print(powerDeg(float(x), y))