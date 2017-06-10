from collections import OrderedDict
n = int(input())
sold = OrderedDict()

for i in range(n):
    l = input().split()
    item = ' '.join(l[:-1]) # Could also use l.pop()
    price = int(l[-1])
    total = sold.get(item, 0) + int(price)
    sold[item] = total
    
for key, sum in sold.items():
    print(key, sum)
