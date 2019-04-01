import math

a = int(input())

cnt = 1

while cnt <= a:
    cnt += 1
    if(a % cnt == 0):
        print(cnt)
        break