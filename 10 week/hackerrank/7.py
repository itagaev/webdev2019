if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

max = -110

for x in arr:
    if(max < x):
        max = x

secmax = -110
for x in arr:
    if max == x:
        continue
    if secmax < x:
        secmax = x

print(secmax)