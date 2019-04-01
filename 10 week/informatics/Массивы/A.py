arr = []
n = int(input())
inp = input()

list = inp.split(' ')

for s in list:
    arr.append(int(s))

for x in range(0, n, 2):
    print(arr[x], end = " ")