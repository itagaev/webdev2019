n = int(input())
arr = [int (x) for x in input().split()]

isTrue = False;

for index, item in enumerate(arr):     
    if(index > 0):
         if(arr[index] * arr[index - 1] > 0):
             isTrue = True;
             break;

print("YES" if isTrue else "NO")