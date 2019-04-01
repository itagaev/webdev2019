n = int(input())
arr = [int (x) for x in input().split()]

cnt = 0

for index, item in enumerate(arr):
    if index > 0:
        if arr[index] > arr[index - 1]:
            cnt += 1

print(cnt)