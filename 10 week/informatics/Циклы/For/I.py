import math

a = int(input())

cnt = 0

for x in range(1, int(math.sqrt(a))):
    if(a % x == 0):
        cnt = cnt + 1
cnt *= 2
print(cnt + 1 if a % math.sqrt(a) == 0 else cnt)

