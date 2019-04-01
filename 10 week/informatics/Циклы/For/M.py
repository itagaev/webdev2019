import math

cnt = 0

n = int(input())

for x in range(0, n):
    a = int(input())
    if a == 0:
        cnt += 1

print(cnt)
