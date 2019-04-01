n = int(input())
arr = [int (x) for x in input().split()]

cnt = 0

for x in range(1, n - 1):
    if arr[x] > arr[x - 1] and arr[x] > arr[x + 1]:
        cnt += 1
print(cnt)