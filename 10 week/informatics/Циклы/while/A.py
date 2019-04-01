import math

a = int(input())

cnt = 1

while cnt <= math.sqrt(a):
    print(cnt ** 2)
    cnt += 1