from collections import OrderedDict
n = int(input())
words = OrderedDict()
for _ in range(n):
    word = input()
    count = words.get(word, 0) + 1
    words[word] = count
    
print( len(words.items()) )
print( *( words.values() ) )
