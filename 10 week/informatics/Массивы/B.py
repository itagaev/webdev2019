n = int(input())
arr = [int (x) for x in input().split()]

for x in arr:
    if x % 2 == 0:
        print(x, end = " ")