'''
Question: Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: 
C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence.
Example Let us assume the following comma separated input sequence is given to the program: 
100,150,180 The output of the program should be: 18,22,24
'''

class Cal:
    C = 50
    H = 30
    

    def sqare_root (self,D):
        Q = []
        self.D = D
        for i in range (len(D)):
            Q.append(int(((2 * self.C * int(D[i])) / self.H) ** 0.5))
        return Q

n = input("Enter comma seperated input: ")
l = list(n.split(","))
print (l)
c = Cal()
print (c.sqare_root(l))

