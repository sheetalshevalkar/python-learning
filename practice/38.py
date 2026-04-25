'''
Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program:
 Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
'''
n = "hello World! 123"
s = 0
num = 0
for i in n:
    if i.isupper() :
        s = s + 1
    if i.islower():
        num = num + 1
    else:
        continue
print(f"UPPER {s} LOWER {num}")