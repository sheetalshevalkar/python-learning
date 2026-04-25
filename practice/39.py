'''
Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
 Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
'''
#=======================================
def cal(n):
    sum = 0
    stm = ""
    for i in range(1,5):
        stm = str(n)+ stm
        sum = sum + int(stm)
    return sum

s= cal(9)
print(s)

