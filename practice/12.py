#Exercise 19. Armstrong Number Check
n = 154
num = n
t = 1
c = 0
while n > 0:
    t= n % 10
    c = c + t**3
    n = n//10
if n == c:
    print (f" {num} is Armstrong")
else:
    print (f" {num} is not Armstrong")



