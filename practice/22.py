'''Question: Write a program which can compute the factorial of a given numbers.
  The results should be printed in a comma-separated sequence on a single line. 
  Suppose the following input is supplied to the program: 8 Then, the output should be: 40'''

n =8
l = []
f =1
for i in range(1,n+1):
    f = f*i
    l.append(str(f))
print(",".join(l))
    


    #...........
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

print(fact(8))