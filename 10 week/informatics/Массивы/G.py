n = int(input())
arr = [int (x) for x in input().split()]
cnt = 1
for x in range(0, n):
    print(arr[n - cnt], end = " ")
    cnt += 1