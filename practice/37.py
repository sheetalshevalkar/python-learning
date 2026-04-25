'''
Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
'''

n = "hello world! 123"
s = 0
num = 0
for i in n:
    if i.isalpha() :
        s = s + 1
    if i.isdigit():
        num = num + 1
    else:
        continue
print(f"LETTERS {s} DIGITS {num}")