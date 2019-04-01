import math

a = int(input())

isDegree = False;
cnt = 1

while cnt <= a:
    if cnt == a:
        isDegree = True
        break
    cnt *= 2

print("YES" if isDegree else "NO")  
    