n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append( list( map(int, input().split() )) )

k = int(input())                
                
data.sort( key = lambda sublist : sublist[k]  )

for i in range(len(data)):
    print(*data[i])
