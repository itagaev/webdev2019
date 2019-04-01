def findmin(a, b, c, d):
    a = a if a < b else b
    c = c if c < d else d
    return c if c < a else a

numbers = [int (x) for x in input().split()]

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

