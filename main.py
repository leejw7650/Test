n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

max1 = data[-1]
max2 = data[-2]

list = []

while(len(list) != n):
    for i in range(k):
        list.append(max1)
        if len(list) == n :
            break
    list.append(max2)

print(sum(list))