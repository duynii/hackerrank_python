from itertools import combinations
ss, k = input().split()
ss = list(ss)
ss.sort()
k = int(k)

for i in range(1, k+1):
    for j in combinations(ss,i):
        print( ''.join(j) )
