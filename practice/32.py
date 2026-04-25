'''
Level 2

Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. 
Suppose the following input is supplied to the program:
 without,hello,bag,world Then, the output should be: bag,hello,without,world
'''

# class Sorting:
#     def __init__(self):
#         pass
#     def alfa(self,n):
#         self.n = n

#     def sortWord(self):
#         self.n.sort()
#         print(','.join(self.n))
 

# my_string = Sorting()
# my_string.alfa(["fish","hat","cat","letter"])
# my_string.sortWord()

l= ["fish","hat","cat","letter"]
print (l.sort())
print(','.join(l))