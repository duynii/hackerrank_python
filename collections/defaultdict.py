#!/usr/bin/python3
from collections import defaultdict
n, m = map(int, input().split())

group_a = defaultdict(list)
for i in range(1,n+1):
    group_a[input()].append(i)
    
for b in range(m):
    print( *group_a.get(input(), [-1]) ) # if no item, returns default list [-1]
