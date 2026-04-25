'''
Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: 
hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world
'''
accept = input (" Enter whitespace separated words: ")
l = list(accept.split(" "))
t = []
# print(l)
temp = ''
for i in range(len(l)):
    if l[i] not in t:
        t.append( l[i].lower())
        temp = l[i]


print(t)
t.sort()  
print(','.join(t))


# short form
words = input().split()
print(' '.join(sorted(set(words))))
