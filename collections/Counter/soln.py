#!/usr/bin/python3
from collections import Counter
shoes_num = int(input())
sizes = list(map(int, input().split()))

customers_count = int(input())

counter = Counter(sizes)
#print( counter )

money = 0
for i in range(customers_count):
    size, price = map(int, input().split())
    if size in counter and counter[size] > 0:
        #print("{} {}".format(size, price) )
        counter[size] -= 1
        money += price
        
print( money )
