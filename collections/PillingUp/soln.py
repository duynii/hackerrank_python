from collections import deque
n = int(input())

deq = deque()
for _ in range(n):
    ops = input().split()    
    op = ops[0]
    if op == 'append':
        deq.append( int(ops[-1]) )
    elif op == 'appendleft':
        deq.appendleft( int(ops[-1]) )
    elif op == 'pop':
        deq.pop()
    else:
        deq.popleft()            
                   
print(*deq)
