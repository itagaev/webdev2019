def bool1(x, y):
    if (x == 0 and y == 0) or (x == 1 and y == 1):
        return 0
    else: 
        return 1

numbers = [int (x) for x in input().split()]

print(bool1(numbers[0], numbers[1]))

