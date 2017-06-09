#!/usr/bin/python3

from itertools import combinations
n = int(input())
ll = list(input().split())
k = int(input())

indices = list( range(n) )
#print( indices )

comb = list( combinations(indices, k) )
#print( comb )

has_a = set()
for i in range(n):
    if( ll[i] == 'a' ):
        has_a.add(i)
        
#print(has_a)

count = 0
for a in comb:
    if has_a & set(a):
        count += 1
        
print(  count/len(comb) )
