#!/usr/bin/python3

from itertools import combinations
n = int(input())
ll = list(input().split())
k = int(input())

indices = list( range(n) )
#print( indices )

comb = list( combinations(indices, k) )
#print( comb )

# has_a = set()
# for i in range(n):
#     if( ll[i] == 'a' ):
#         has_a.add(i)
        
has_a = set( filter( lambda i : ll[i] == 'a' , range(n) ) )
#print( has_a )       
    
#print(has_a)

# count = 0
# for a in comb:
#     if has_a & set(a):
#         count += 1
        
# print(  count/len(comb) )
        
a_list = list( filter( lambda x : set(x) & has_a, comb) )

print( len(a_list) / len(comb) )
