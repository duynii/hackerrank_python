n, x = map(int, input().split())
# Using list comprehension, same speed
# n, x = [int(x) for x in input().split()]

subjects = []
for _ in range(x):
    subjects.append( list(map(float, input().split())) )
    
for tup in zip(*subjects):
    print( sum(tup) / len(tup) )

# Alternative one liner
# [print(sum(i) / len(i) ) for i in zip( *[map(float, input().split()) for _ in range(int(input().split()[1])) ] ) ]
